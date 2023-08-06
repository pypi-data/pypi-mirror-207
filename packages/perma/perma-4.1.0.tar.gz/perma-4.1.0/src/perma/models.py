import re


# Django
import modelcluster.models
from django.db import models as django_models
from django.db.models import ForeignKey
from django.conf import settings
from django.db import transaction
from django.core.exceptions import ValidationError
from django.http import Http404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, get_language_from_request
from django.utils.functional import cached_property, classproperty
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.shortcuts import redirect

# Wagtail

from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path
from wagtail.models import (Page, Orderable, TranslatableMixin, DraftStateMixin, RevisionMixin, PreviewableMixin, Site,
                            Locale)

from wagtail.rich_text import RichText
from wagtail_preference_blocks.decorators import provides_preferences_context

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TagBase, ItemBase

from django_auxiliaries.validators import python_identifier_validator
from django_auxiliaries.variable_scope import WagtailPageMixin, reset_variable_scopes, load_variable_scope
from django_auxiliaries.servable import Servable

from wagtail_synopsis.models import AUTHOR_ROLE, build_synopsis_class_for
from wagtail_synopsis.curation import register_synopsis_category

from officekit.models import Person, Organisation, GroupMember
from tour_guide.anchors import AnchorRegistry
from tour_guide.decorators import chooses_navigation_categories

# Panels

from wagtail.admin.panels import (FieldPanel, InlinePanel, TabbedInterface, ObjectList)


# Registration Decorators

from wagtail.utils.decorators import cached_classmethod

from .model_fields import RecordDescriptionField
from .blocks import RecordBlock, ResourceBlock, ResourceBlockValue, RequirementBlock, RequirementBlockValue

from .html_to_text import html_to_text

from wagtail_block_model_field.fields import BlockModelField

from .apps import get_app_label
from .wagtail_settings import PermaSiteSettings
from .utilities import record_identifier_validator, record_keygen, RECORD_KEY_LENGTH, RECORD_KEY_ALPHABET
from .views import RecordViewSet

APP_LABEL = get_app_label()


class RecordTag(TagBase):
    class Meta:
        verbose_name = "record tag"
        verbose_name_plural = "record tags"


class RecordTagItem(ItemBase):

    class Meta:

        # constraints = [
        #    django_models.UniqueConstraint('content_object',
        #                                   'tag', name='unique_%(app_label)s_%(class)s.unique_tag_assignment')
        #]

        unique_together = (('content_object', 'tag'),)

    tag = django_models.ForeignKey(
        RecordTag, related_name="tagged_record", on_delete=django_models.CASCADE
    )

    content_object = ParentalKey(
        to=APP_LABEL + '.Record',
        on_delete=django_models.CASCADE,
        related_name='tagged_items'
    )


def create_record_tag(*, tag, content_object):
    return RecordTagItem(tag=tag, content_object_id=content_object.id)


def text_from_rich_text(rich_text):
    return html_to_text(rich_text.source)


SENTENCE_RE = re.compile(r'\.[ \t\n\r]+[A-Z]')


def extract_record_description_text(record):

    for stream_child in record:
        if stream_child.block_type != 'text':
            continue

        text = text_from_rich_text(stream_child.value)
        match = SENTENCE_RE.search(text)

        if match:
            text = text[:match.start() + 1]

        return text

    return ''


RECORD_SYNOPSIS_CATEGORY = register_synopsis_category(APP_LABEL, 'record', 'Record')


class AbstractRecord(WagtailPageMixin, TranslatableMixin,
                     DraftStateMixin, RevisionMixin, AnchorRegistry, PreviewableMixin, Servable):

    class Meta:
        abstract = True
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    template = APP_LABEL + "/record_page.html"

    preview_template = APP_LABEL + "/record_page.html"
    ajax_preview_template = None

    RECORD_BLOCK = RecordBlock(label="Record")

    key = django_models.CharField(max_length=RECORD_KEY_LENGTH, validators=(record_identifier_validator,))

    live = django_models.BooleanField(verbose_name=_("live"), default=False, editable=True)

    created_by_user = django_models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by user'),
        null=True,
        blank=True,
        editable=False,
        on_delete=django_models.SET_NULL
    )

    description = RecordDescriptionField(
                blank=True,
                help_text=
                "A description of the contents of this record.")

    tags = ClusterTaggableManager(through=APP_LABEL + '.RecordTagItem', blank=True)

    content_panels = [
        FieldPanel('key', heading="Key"),
        FieldPanel('live', heading="Is Live?"),
        InlinePanel('authors', heading="Authors"),
        FieldPanel('tags', heading="Tags"),
        FieldPanel('description', heading="Record"),
        InlinePanel('resources', heading="Resources"),
        InlinePanel('requirements', heading="Requirements"),
    ]

    @cached_property
    def author_names(self):

        authors = [author.author.specific for author in self.authors.all()] # noqa
        authors = [author for author in authors if author]
        value = self.RECORD_BLOCK.child_blocks['authors'].value_from_group_members(authors) # noqa
        result = self.RECORD_BLOCK.child_blocks['authors'].render(value)
        return result

    @property
    def record_synopsis(self):

        if self.synopsis and self.synopsis.count() > 0: # noqa
            return self.synopsis.first() # noqa

        return None

    @property
    def as_block_value(self):
        return self.RECORD_BLOCK.value_for_record(self)

    def get_context(self, request):

        context = super().get_context(request)

        env = {
            'request': request,
            'page': None
        }

        reset_variable_scopes(env)

        load_variable_scope("tour_guide", anchor_registry=self)

        preferences_context = getattr(self, 'preferences_context', None)

        context.update({
            'record': self,
            'page_template': settings.PERMA_RECORD_PAGE_TEMPLATE,
            'preferences': preferences_context,
        })

        return context

    def get_preview_context(self, request, mode_name):

        context = super(AbstractRecord, self).get_preview_context(request, mode_name)

        context.update(
            self.get_context(request)
        )

        return context

    def get_preview_template(self, request, mode_name):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return self.ajax_preview_template or self.preview_template
        else:
            return self.preview_template

    def render(self, request):

        template = self.get_template(request)
        context = self.get_context(request)

        result = render_to_string(template, context=context, request=request)
        return result

    def sync_synopsis(self, synopsis):

        synopsis.category = RECORD_SYNOPSIS_CATEGORY.identifier

        synopsis.rubric = ''
        synopsis.rubric_url = ''

        if not synopsis.summary:
            synopsis.summary = RichText(extract_record_description_text(self.description)) # noqa

        authors = [author.author.specific for author in self.authors.all()] # noqa
        authors = [author for author in authors if author]
        value = self.RECORD_BLOCK.child_blocks['authors'].json_from_group_members(authors) # noqa
        value['role'] = AUTHOR_ROLE

        synopsis.names = value

    def determine_url(self, request, current_site=None):
        return ''

    def __str__(self):
        return f'[{self.key}] {self.title}' # noqa


@provides_preferences_context
class Record(AbstractRecord, modelcluster.models.ClusterableModel):

    class Meta:
        unique_together = [("key", "locale"), ("translation_key", "locale")]

    title = django_models.CharField(
        verbose_name=_("title"),
        max_length=255,
        help_text=_("The record title as you'd like it to be seen by the public"),
    )

    seo_title = django_models.CharField(
        verbose_name=_("title tag"),
        max_length=255,
        blank=True,
        help_text=_(
            "The name of the page displayed on search engine results as the clickable headline."
        ),
    )

    search_description = django_models.TextField(
        verbose_name=_("meta description"),
        blank=True,
        help_text=_(
            "The descriptive text displayed underneath a headline in search engine results."
        ),
    )

    content_panels = [
        FieldPanel('title', heading="Title", classname="title"),
        FieldPanel('tags', heading="Tags")
    ] + AbstractRecord.content_panels

    promote_panels = [
        FieldPanel('seo_title'),
        FieldPanel('search_description')
    ]

    def full_clean(self, *args, **kwargs):

        if self.key is None:
            self.key = record_keygen()

        # Set the locale
        if self.locale_id is None:
            self.locale = self.get_default_locale()

        super().full_clean(*args, **kwargs)

    def clean(self):
        super().clean()

        queryset = Record.objects.all().filter(key=self.key)

        if self.id:
            queryset = queryset.exclude(id=self.id)

        if queryset.exists():
            raise ValidationError({"key": _("This key is already in use")})

    @transaction.atomic
    def save(self, update_fields=None, clean=True, **kwargs):

        did_update_key = not self.key

        if clean:
            self.full_clean()

        if update_fields is not None:
            update_fields_index = frozenset(update_fields)

            if 'key' not in update_fields_index and did_update_key:
                update_fields.append('key')

        super().save(update_fields=update_fields, **kwargs)

    def sync_synopsis(self, synopsis):
        super(Record, self).sync_synopsis(synopsis)

        synopsis.heading = self.title
        synopsis.created_at = self.first_published_at or timezone.now()
        synopsis.updated_at = self.last_published_at

    def determine_url(self, request, current_site=None):

        if current_site is None:
            current_site = Site.find_for_request(request)

        if current_site is None:
            current_site = Site.objects.get(is_default_site=True)

        perma_settings = PermaSiteSettings.for_site(current_site)

        if not perma_settings.canonical_record_index_page or not self.first_published_at:
            return ''

        result = perma_settings.canonical_record_index_page.get_url(request=request, current_site=current_site)
        result = f"{result}{self.key}/"
        return result

    _edit_handler = None

    @classproperty
    def edit_handler(cls):

        if cls._edit_handler:
            return cls._edit_handler

        tabs = []

        if cls.content_panels:
            tabs.append(ObjectList(cls.content_panels, heading=_("Content")))

        synopsis_adapter = RecordSynopsis.install_synopsis_adapter_for(
            editable_fields=['summary', 'visual'],
            sync_method=Record.sync_synopsis,
            tagged_item_class=RecordTagItem,
            tags_field='tags',
            tagged_items_field='tagged_items'
        )

        tabs.append(synopsis_adapter.create_synopsis_panel_for(cls))

        if cls.promote_panels:
            tabs.append(ObjectList(cls.promote_panels, heading=_("Promote")))

        edit_handler = TabbedInterface(tabs)

        bound_handler = edit_handler.bind_to_model(cls)
        cls._edit_handler = bound_handler
        return bound_handler


Record = register_snippet(Record, viewset=RecordViewSet)


class RecordAuthor(Orderable):

    class Meta(Orderable.Meta):
        verbose_name = 'Author in Record'
        verbose_name_plural = 'Authors in Record'
        unique_together = (('author', 'record'),)

    record = ParentalKey(Record, related_name="authors", on_delete=django_models.CASCADE, blank=False)
    author = ForeignKey(GroupMember, related_name="records", on_delete=django_models.CASCADE, blank=False)

    panels = [
        FieldPanel('record'),
        FieldPanel('author'),
    ]

    def __str__(self):
        author = self.author.specific # noqa

        if isinstance(author, Person):
            name = author.full_name
        elif isinstance(author, Organisation):
            name = author.name
        else:
            name = '[unknown group member type]'

        return f"{name} in {self.record.title}" # noqa


class RecordResource(Orderable):

    class Meta(Orderable.Meta):
        verbose_name = 'Record Resource'
        verbose_name_plural = 'Record Resource'
        unique_together = (('record', 'identifier'),)

    record = ParentalKey(Record, related_name="resources", on_delete=django_models.CASCADE, blank=False)

    identifier = django_models.CharField(max_length=128, blank=False, null=False,
                                         default='', validators=[python_identifier_validator])

    definition = BlockModelField(ResourceBlock(), value_class=ResourceBlockValue)

    panels = [
        FieldPanel('record'),
        FieldPanel('identifier'),
        FieldPanel('definition'),
    ]

    def __str__(self):

        return f"{self.identifier} in {self.record.title}" # noqa


class RecordRequirement(Orderable):

    class Meta(Orderable.Meta):
        verbose_name = 'Requirement in Record'
        verbose_name_plural = 'Requirement in Record'
        unique_together = (('record', 'identifier'),)

    record = ParentalKey(Record, related_name="requirements", on_delete=django_models.CASCADE, blank=False)

    identifier = django_models.CharField(max_length=128, blank=False, null=False,
                                         default='', validators=[python_identifier_validator])

    definition = BlockModelField(RequirementBlock(), value_class=RequirementBlockValue)

    panels = [
        FieldPanel('record'),
        FieldPanel('identifier'),
        FieldPanel('definition'),
    ]

    def __str__(self):

        return f"{self.identifier} in {self.record.title}" # noqa


RecordSynopsis = build_synopsis_class_for(Record)


@chooses_navigation_categories
class RecordIndexPage(RoutablePageMixin, AnchorRegistry, Page):

    class Meta:
        verbose_name = "Record Index Page"
        verbose_name_plural = "Record Index Pages"

    template = APP_LABEL + "/record_index_page.html"
    default_redirect_target = settings.PERMA_RECORD_INDEX_REDIRECT_TARGET

    @path('')
    def default_view(self, request):

        if self.default_redirect_target:
            return redirect(self.default_redirect_target, permanent=False)

        if settings.PERMA_RECORD_INDEX_NOT_ACCESSIBLE:
            raise Http404('Not found.')

        return self.index_route(request)

    @re_path(f'(?P<record_key>[{"".join(RECORD_KEY_ALPHABET)}]{{{RECORD_KEY_LENGTH}}})/')
    def serve_record(self, request, record_key):

        language = get_language_from_request(request)

        try:
            locale = Locale.objects.get_for_language(language)
        except Locale.DoesNotExist:
            locale = Locale.get_active()

        try:
            record = Record.objects.get(live=True, key__exact=record_key, locale_id=locale.id)

        except Record.DoesNotExist:

            try:
                locale = Locale.objects.get_for_language('en')
            except Locale.DoesNotExist:
                locale = None

            records = Record.objects.filter(live=True, key__exact=record_key, locale_id=locale.id).order_by('locale__language_code')

            if not records.exists():
                raise Http404('Not found.')

            record = records.first()

        return record.serve(request)
