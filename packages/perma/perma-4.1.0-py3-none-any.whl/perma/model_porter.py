
from model_porter.config import ModelPorterConfig
from model_porter.support_mixin import ModelPorterSupportMixin
from model_porter.utilities import define_tags as define_generic_tags

from officekit.models import GroupMember

from .models import RecordAuthor, RecordResource, RecordRequirement, RecordTag, RecordTagItem


def link_authors(*, identifiers, context):

    record = context.get_variable(context.INSTANCE_VARIABLE)
    result = []

    for identifier in identifiers:
        author = GroupMember.objects.get(identifier=identifier)

        if author is None:
            continue

        by = RecordAuthor()
        by.record = record
        by.author_id = author.id

        result.append(by)

    return result


RESOURCE_BLOCK = RecordResource.definition.field.block_def


def define_resources(*, definitions, context):

    record = context.get_variable(context.INSTANCE_VARIABLE)
    result = []

    for definition in definitions:

        if isinstance(RESOURCE_BLOCK, ModelPorterSupportMixin):
            definition = RESOURCE_BLOCK.from_repository(definition, context)

        definition = RESOURCE_BLOCK.to_python(definition)

        resource = RecordResource()

        if resource is None:
            continue

        resource.record = record
        resource.identifier = definition.identifier
        resource.definition = definition

        result.append(resource)

    return result


REQUIREMENT_BLOCK = RecordRequirement.definition.field.block_def


def define_requirements(*, definitions, context):

    record = context.get_variable(context.INSTANCE_VARIABLE)
    result = []

    for definition in definitions:

        if isinstance(REQUIREMENT_BLOCK, ModelPorterSupportMixin):
            definition = REQUIREMENT_BLOCK.from_repository(definition, context)

        definition = REQUIREMENT_BLOCK.to_python(definition)

        requirement = RecordRequirement()

        if requirement is None:
            continue

        requirement.record = record
        requirement.identifier = definition.identifier
        requirement.definition = definition

        result.append(requirement)

    return result


def define_tags(*, tag_values, context):
    return define_generic_tags(tag_values=tag_values, tag_class=RecordTag, tag_item_class=RecordTagItem, context=context)


def publish_record(*, instance, context):
    instance.save()
    revision = instance.save_revision(log_action=False)
    revision.publish()
    instance.refresh_from_db()
    return instance


class PermaConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(PermaConfig, self).__init__(app_label, module)
        self.register_function_action(link_authors, context_argument='context')
        self.register_function_action(define_resources, context_argument='context')
        self.register_function_action(define_requirements, context_argument='context')
        self.register_function_action(define_tags, context_argument='context')
        self.register_function_action(publish_record, context_argument='context')

