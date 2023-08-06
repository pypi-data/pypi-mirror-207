
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property

from wagtail import blocks
from wagtail.blocks import RichTextBlock
from wagtail.blocks.struct_block import StructBlockAdapter

from wagtail.telepath import register
from wagtail.admin.staticfiles import versioned_static

from wagtail.embeds import blocks as embed_blocks
from wagtail.documents import blocks as document_blocks

from django_auxiliaries.validators import python_identifier_validator
from wagtail_switch_block.blocks import SwitchBlock, SwitchValue, DynamicSwitchBlock
from wagtail_switch_block.block_registry import BlockRegistry

from wagtail_tags_block.blocks import TagsBlock, TagsValue

from officekit.blocks import NameListBlock
from figurative.blocks import FigureBlock, SlideshowBlock

from .apps import get_app_label


__all__ = ['RecordDescriptionBlock', 'RecordDescriptionValue', 'RecordTagsBlock', 'RecordTagsBlockValue',
           'RecordBlock', 'RecordBlockValue', 'ResourceBlock', 'ResourceBlockValue', 'RESOURCE_BLOCK_REGISTRY',
           'BaseResourceBlock', 'RequirementBlock', 'RequirementBlockValue', 'REQUIREMENT_BLOCK_REGISTRY',
           'BaseRequirementBlock']

APP_LABEL = get_app_label()


class ResourceBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        if not issubclass(block_type, BaseResourceBlock):
            raise RuntimeError("Registered block type must be a subclass of BaseResourceBlock")

        return True

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_container_block(self, identifier, entry, container_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, container_block):
        block_kwargs = dict(entry.block_kwargs)

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


RESOURCE_BLOCK_REGISTRY = ResourceBlockRegistry()
RESOURCE_BLOCK_REGISTRY.define_procedures_in_caller_module("resource")


class BaseResourceBlock(blocks.StructBlock):

    identifier = blocks.CharBlock(max_length=128, required=False, default='', validators=[python_identifier_validator])
    name = blocks.CharBlock(max_length=128, required=False, default='')
    has_access_restrictions = blocks.BooleanBlock(default=False, required=False)
    description = blocks.TextBlock(max_length=512, required=False, default='')


class ResourceBlockAdapter(StructBlockAdapter):

    def js_args(self, block):
        name, nested, options = super().js_args(block)
        return [name, list(nested)[1:], options]


register(ResourceBlockAdapter(), BaseResourceBlock)


class ResourceBlockValue(SwitchValue):

    @property
    def identifier(self):
        return self.value['identifier']


class ResourceBlock(DynamicSwitchBlock):

    class Meta:
        value_class = ResourceBlockValue
        resource_blocks_function_name = APP_LABEL + ".blocks.resource_block_choices"
        choice_label = "Select Resource"

    def __init__(self, *args, **kwargs):

        resource_blocks_function_name = kwargs.pop("resource_blocks_function_name",
                                                     self._meta_class.resource_blocks_function_name) # noqa

        super().__init__(*args,
                         resource_blocks_function_name=resource_blocks_function_name,
                         child_blocks_function_name=resource_blocks_function_name,
                         **kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class LocatorValue(SwitchValue):

    def as_url(self):

        if self.type == 'url':
            return self.value
        elif self.type == 'document':

            if not self.value:
                return ''

            result = reverse("wagtaildocs_serve", args=(self.value.pk, self.value.filename))
            return result

        return ''


class LocatorBlock(SwitchBlock):

    class Meta:
        value_class = LocatorValue

    none = blocks.StaticBlock()
    url = blocks.URLBlock(max_length=512)
    document = document_blocks.DocumentChooserBlock()


class EncodingBlock(SwitchBlock):
    pass



class CompressionBlock(SwitchBlock):

    pass


class FileResourceBlock(BaseResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/file_block.html"
        description = "File"

    location = LocatorBlock()
    file_size = blocks.IntegerBlock("File Size")


register_resource_block(APP_LABEL, "file", FileResourceBlock, [], {}) # noqa


class BinaryFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/binary_file_block.html"
        description = "Binary File"

register_resource_block(APP_LABEL, "binary_file", BinaryFileBlock, [], {}) # noqa


class TextFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/text_file_block.html"
        description = "Text File"

register_resource_block(APP_LABEL, "text_file", TextFileBlock, [], {}) # noqa


class CSVFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/csv_file_block.html"
        description = "Comma Separated Value File"

register_resource_block(APP_LABEL, "csv_file", CSVFileBlock, [], {}) # noqa


class ExcelFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/excel_file_block.html"
        description = "Microsoft Excel File"

register_resource_block(APP_LABEL, "excel_file", ExcelFileBlock, [], {}) # noqa


class XMLFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/xml_file_block.html"
        description = "XML File"

register_resource_block(APP_LABEL, "xml_file", XMLFileBlock, [], {}) # noqa


class JSONFileBlock(FileResourceBlock):

    class Meta:
        template = APP_LABEL + "/blocks/json_file_block.html"
        description = "JSON File"

register_resource_block(APP_LABEL, "json_file", JSONFileBlock, [], {}) # noqa


class RequirementBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_register_block(self, app_label, local_identifier, block_type, block_args, block_kwargs, **kwargs):
        if not issubclass(block_type, BaseRequirementBlock):
            raise RuntimeError("Registered block type must be a subclass of BaseRequirementBlock")

        return True

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_container_block(self, identifier, entry, container_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, container_block):
        block_kwargs = dict(entry.block_kwargs)

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


REQUIREMENT_BLOCK_REGISTRY = RequirementBlockRegistry()
REQUIREMENT_BLOCK_REGISTRY.define_procedures_in_caller_module("requirement")


class BaseRequirementBlock(blocks.StructBlock):

    identifier = blocks.CharBlock(max_length=128, required=False, default='', validators=[python_identifier_validator])
    name = blocks.CharBlock(max_length=128, required=False, default='')
    description = blocks.CharBlock(max_length=512, required=False, default='')


class RequirementBlockAdapter(StructBlockAdapter):

    def js_args(self, block):
        name, nested, options = super().js_args(block)
        return [name, list(nested)[1:], options]


register(RequirementBlockAdapter(), BaseRequirementBlock)


class RequirementBlockValue(SwitchValue):

    @property
    def identifier(self):
        return self.value['identifier']


class RequirementBlock(DynamicSwitchBlock):

    class Meta:
        value_class = RequirementBlockValue
        requirement_blocks_function_name = APP_LABEL + ".blocks.requirement_block_choices"
        choice_label = "Select Requirement"

    def __init__(self, *args, **kwargs):

        requirement_blocks_function_name = kwargs.pop("requirement_blocks_function_name",
                                                     self._meta_class.requirement_blocks_function_name) # noqa

        super().__init__(*args,
                         requirement_blocks_function_name=requirement_blocks_function_name,
                         child_blocks_function_name=requirement_blocks_function_name,
                         **kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class SoftwareRequirementBlock(BaseRequirementBlock):

    class Meta:
        template = APP_LABEL + "/blocks/software_requirement_block.html"
        description = "Required Software"

    location = LocatorBlock()


register_requirement_block(APP_LABEL, "software_requirement", SoftwareRequirementBlock, [], {}) # noqa


RecordDescriptionValue = blocks.StreamValue


class RecordDescriptionBlock(blocks.StreamBlock):

    class Meta:
        icon = 'form'
        container_element = None
        default = []
        template = APP_LABEL + '/blocks/record_description_block.html'

    text = RichTextBlock(label='Text',
                         editor=APP_LABEL + '.richtextarea',  # noqa
                         required=False,
                         help_text=("Use a text block for writing a sequence of paragraphs and to "
                                    "apply semantic styles. Paragraphs are defined by inserting "
                                    "line breaks from the editor toolbar."))

    figure = FigureBlock(label='Figure', help_text="Present visual media in a figure.", required=False)
    slideshow = SlideshowBlock(label='Slideshow', help_text="Present visual media as a slideshow",
                               required=False)

    embed = embed_blocks.EmbedBlock(label="Embed", required=False)

    def to_python(self, value):

        value = blocks.StreamBlock.to_python(self, value)
        return value

    def get_prep_value(self, value):

        value = blocks.StreamBlock.get_prep_value(self, value)
        return value

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        path = APP_LABEL + '.ResourceDescriptionBlock'
        return path, [], kwargs


RecordTagsBlockValue = TagsValue


class RecordTagsBlock(TagsBlock):

    class Meta:
        template = APP_LABEL + '/blocks/record_tags_block.html'
        tag_model = APP_LABEL + ".recordtag"

        classname = settings.PERMA_RECORD_TAGS_BLOCK_CLASSNAME
        tag_classname = settings.PERMA_RECORD_TAGS_BLOCK_TAG_CLASSNAME
        container_element = settings.PERMA_RECORD_TAGS_BLOCK_CONTAINER_ELEMENT


RecordDatesBlockValue = blocks.StructValue


class RecordDatesBlock(blocks.StructBlock):

    class Meta:
        template = APP_LABEL + '/blocks/record_dates_block.html'

    first_published_at = blocks.DateBlock(label="First Published", required=False, default={})
    last_published_at = blocks.DateBlock(label="Last Published", required=False, default={})


class RecordResourcesBlock(blocks.StreamBlock):

    class Meta:
        template = APP_LABEL + "/blocks/record_resources_block.html"

    resource = ResourceBlock()


class RecordRequirementsBlock(blocks.StreamBlock):

    class Meta:
        template = APP_LABEL + "/blocks/record_requirements_block.html"

    requirement = RequirementBlock()


RecordBlockValue = blocks.StructValue


class RecordBlock(blocks.StructBlock):

    class Meta:
        classname = settings.PERMA_RECORD_BLOCK_CLASSNAME
        template = APP_LABEL + '/blocks/record_block.html'

    record = blocks.StaticBlock() # placeholder

    title = blocks.CharBlock(required=False)
    dates = RecordDatesBlock(required=False)

    authors = NameListBlock(required=False, classname=settings.PERMA_RECORD_BLOCK_AUTHORS_CLASSNAME,
                            container_element="ol", template=APP_LABEL + "/blocks/record_authors_block.html")

    tags = RecordTagsBlock(required=False)
    description = RecordDescriptionBlock(required=False)
    resources = RecordResourcesBlock(rquired=False)
    requirements = RecordRequirementsBlock(required=False)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def value_for_record(self, record):

        authors = self.child_blocks['authors'].value_from_group_members(
            [assignment.author for assignment in record.authors.all()])

        tags = [tag.name for tag in record.tags.all()]
        tags = self.child_blocks['tags'].to_python(tags)

        resources = []
        resource_block = self.child_blocks['resources'].child_blocks['resource']

        for assignment in record.resources.all():
            definition = resource_block.get_prep_value(assignment.definition)
            definition[assignment.definition.type]['identifier'] = assignment.identifier
            definition = resource_block.to_python(definition)
            resources.append(('resource', definition))

        resources = blocks.StreamValue(self.child_blocks['resources'], resources, is_lazy=False, raw_text=None)

        requirements = []
        requirement_block = self.child_blocks['requirements'].child_blocks['requirement']

        for assignment in record.requirements.all():
            definition = requirement_block.get_prep_value(assignment.definition)
            definition[assignment.definition.type]['identifier'] = assignment.identifier
            definition = requirement_block.to_python(definition)
            requirements.append(('requirement', definition))

        requirements = blocks.StreamValue(self.child_blocks['requirements'], requirements, is_lazy=False, raw_text=None)

        dates = {
            "first_published_at": record.first_published_at,
            "last_published_at": record.last_published_at
        }

        dates = self.child_blocks['dates'].to_python(dates)

        value = blocks.StructValue(self, {
            "record": record,
            "title": record.title,
            "dates": dates,
            "authors": authors,
            "tags": tags,
            "description": record.description,
            "resources": resources,
            "requirements": requirements
        })

        return value
