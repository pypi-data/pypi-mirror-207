import weakref

from django.conf import settings

from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


from wagtail_switch_block import SwitchBlock, DynamicSwitchBlock
from wagtail_switch_block.block_registry import BlockRegistry

from wagtail_dynamic_choice.blocks import AlternateSnippetChooserBlock

from wagtail_content_admin.blocks import (ContentBlock, ContentBlockValue, register_content_block)

from querykit.base import *
from querykit.forms import PickerFactory

from aldine.blocks import BaseContentLayoutBlock
from figurative.blocks import FigureBlock, SlideshowBlock

from .address_formats import lookup_address_format, PHYSICAL_ADDRESS_FORMAT_PLAIN

from .apps import get_app_label


__all__ = ['AddressChooserBlock', 'FormattedAddressBlock',
           'GroupAssignmentChooserBlock', 'GroupAssignmentChooserBlockValue',
           'GroupMemberChooserBlock', 'GroupMemberChooserBlockValue',
           'GroupChooserBlock', 'GroupChooserBlockValue',
           'GroupAssignmentsBlock', 'GroupMembersBlock', 'GroupsBlock',
           'GroupAssignmentLayoutBlock', 'GroupMemberLayoutBlock', 'GroupLayoutBlock',
           'GroupAssignmentListBlock', 'GroupMemberListBlock', 'GroupListBlock',
           'PersonNameBlock', 'OrganisationNameBlock', 'NameListBlock', 'NameListBlockValue']


APP_LABEL = get_app_label()


class AddressChooserBlock(SnippetChooserBlock):

    def __init__(self, **kwargs):

        kwargs.pop('target_model', None)
        super().__init__(target_model=APP_LABEL + ".address", **kwargs)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class FormattedAddressBlock(blocks.StructBlock):

    class Meta:
        template = APP_LABEL + "/blocks/formatted_address_block.html"

    address = AlternateSnippetChooserBlock(target_model=APP_LABEL + ".address")
    format = AlternateSnippetChooserBlock(target_model=APP_LABEL + ".addressformat")
    link_text = blocks.CharBlock(default="", required=False, label="Link Text", help_text="Incorporated by link formats.")

    def __init__(self, **kwargs):

        kwargs.pop('target_model', None)
        super().__init__(target_model=APP_LABEL + ".address", **kwargs)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)

        address = value['address']
        address_format = lookup_address_format(value['format'].method, PHYSICAL_ADDRESS_FORMAT_PLAIN)

        link_text = value['link_text']

        context['address'] = address
        context['formatted_address'] = address_format.function(address, link_text=link_text)

        return context


group_assignment_admin = None


def get_group_assignment_admin():

    global group_assignment_admin

    if group_assignment_admin is None:
        from .frontend import group_assignment_admin

    return group_assignment_admin


def configure_chooser_group_assignment_item(item, instance):
    get_group_assignment_admin().configure_frontend_item(item, instance)


def create_group_assignment_query_parameters():
    fp_factory = PickerFactory()

    parameters = [
        ResultSliceParameter(
               identifier='page',
               widget_factory=None),

        OrderParameter(
               identifier='sort_by',
               label='Sort By',
               widget_factory=None),

        SliceSizeParameter(
               identifier='per_page',
               label='Per Page',
               widget_factory=None),
    ]

    return parameters


class GroupAssignmentsBlock(ContentBlock):

    class Meta:
        verbose_item_name = "Group Assignment"
        verbose_item_name_plural = "Group Assignments"

        chooser_url = APP_LABEL + ":group_assignment_chooser"  # group_assignment_admin.chooser_url_specifier
        configure_function_name = APP_LABEL + '.blocks.configure_chooser_group_assignment_item'
        max_num_choices = None
        chooser_prompts = {
            'add': 'Add Group Assignment',
            'replace': 'Replace Group Assignment'
        }

        chooser_filter = None

        query_field_choices = [
            ('active', 'Active')
        ]
        query_slice_size = 25
        query_parameters = create_group_assignment_query_parameters()
        query_form_classname = settings.OFFICEKIT_GROUP_ASSIGNMENTS_QUERY_FORM_CLASSNAME

    def __init__(self, **kwargs):
        super().__init__(target_model=APP_LABEL + ".groupassignment", **kwargs) # noqa


register_content_block(APP_LABEL, "groupassignments", GroupAssignmentsBlock, [], {},
                       item_type=APP_LABEL + ".groupassignment")


GroupAssignmentChooserBlockValue = ContentBlockValue


class GroupAssignmentChooserBlock(GroupAssignmentsBlock):

    class Meta:
        query_block_class = None


group_member_admin = None


def get_group_member_admin():

    global group_member_admin

    if group_member_admin is None:
        from .frontend import group_member_admin

    return group_member_admin


def configure_chooser_group_member_item(item, instance):
    get_group_member_admin().configure_frontend_item(item, instance)


def create_group_member_query_parameters():
    fp_factory = PickerFactory()

    parameters = [
        ResultSliceParameter(
               identifier='page',
               widget_factory=None),

        OrderParameter(
               identifier='sort_by',
               label='Sort By',
               widget_factory=None),

        SliceSizeParameter(
               identifier='per_page',
               label='Per Page',
               widget_factory=None),
    ]

    return parameters


class GroupMembersBlock(ContentBlock):

    class Meta:

        verbose_item_name = "Group Member"
        verbose_item_name_plural = "Group Members"

        chooser_url = APP_LABEL + ":group_member_chooser"  # group_member_admin.chooser_url_specifier
        configure_function_name = APP_LABEL + '.blocks.configure_chooser_group_member_item'
        max_num_choices = None
        chooser_prompts = {
            'add': 'Add Group Member',
            'replace': 'Replace Group Member'
        }

        chooser_filter = None

        query_field_choices = [
            ('active', 'Active'),
            ('identifier', 'Identifier')
        ]
        query_slice_size = 25
        query_parameters = create_group_member_query_parameters()
        query_form_classname = settings.OFFICEKIT_GROUP_MEMBERS_QUERY_FORM_CLASSNAME

    def __init__(self, **kwargs):
        super().__init__(target_model=APP_LABEL + ".groupmember", **kwargs) # noqa


register_content_block(APP_LABEL, "groupmembers", GroupMembersBlock, [], {}, item_type=APP_LABEL + ".groupmember")


GroupMemberChooserBlockValue = ContentBlockValue


class GroupMemberChooserBlock(GroupMembersBlock):

    class Meta:
        query_block_class = None


group_admin = None


def get_group_admin():

    global group_admin

    if group_admin is None:
        from .frontend import group_admin

    return group_admin


def configure_chooser_group_item(item, instance):
    get_group_admin().configure_frontend_item(item, instance)


def create_group_query_parameters():
    fp_factory = PickerFactory()

    parameters = [
        ResultSliceParameter(
               identifier='page',
               widget_factory=None),

        OrderParameter(
               identifier='sort_by',
               label='Sort By',
               widget_factory=None),

        SliceSizeParameter(
               identifier='per_page',
               label='Per Page',
               widget_factory=None),
    ]

    return parameters


class GroupsBlock(ContentBlock):

    class Meta:

        verbose_item_name = "Group"
        verbose_item_name_plural = "Groups"

        chooser_url = APP_LABEL + ":group_chooser"  # group_admin.chooser_url_specifier
        configure_function_name = APP_LABEL + '.blocks.configure_chooser_group_item'
        max_num_choices = None
        chooser_prompts = {
            'add': 'Add Group',
            'replace': 'Replace Group'
        }

        chooser_filter = None

        query_field_choices = [
            ('active', 'Active'),
            ('identifier', 'Identifier'),
            ('name', 'Identifier')
        ]
        query_slice_size = 25
        query_parameters = create_group_query_parameters()
        query_form_classname = settings.OFFICEKIT_GROUPS_QUERY_FORM_CLASSNAME

    def __init__(self, **kwargs):
        super().__init__(target_model=APP_LABEL + ".group", **kwargs) # noqa


register_content_block(APP_LABEL, "groups", GroupsBlock, [], {}, item_type=APP_LABEL + ".group")


GroupChooserBlockValue = ContentBlockValue


class GroupChooserBlock(GroupsBlock):

    class Meta:
        query_block_class = None


class GroupAssignmentLayoutBlock(BaseContentLayoutBlock):

    class Meta:
        classname = settings.OFFICEKIT_GROUP_ASSIGNMENT_LAYOUT_BLOCK_CLASSNAME
        supported_item_types = [APP_LABEL + ".groupassignment"]

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class GroupAssignmentListBlock(GroupAssignmentLayoutBlock):

    class Meta:
        classname = settings.OFFICEKIT_GROUP_ASSIGNMENT_LIST_BLOCK_CLASSNAME
        template = APP_LABEL + "/blocks/group_assignment_list_block.html"


class GroupMemberLayoutBlock(BaseContentLayoutBlock):

    class Meta:

        classname = settings.OFFICEKIT_GROUP_MEMBER_LAYOUT_BLOCK_CLASSNAME
        member_classname = settings.OFFICEKIT_GROUP_MEMBER_CLASSNAME
        person_classname = settings.OFFICEKIT_GROUP_MEMBER_PERSON_CLASSNAME
        organisation_classname = settings.OFFICEKIT_GROUP_MEMBER_ORGANISATION_CLASSNAME

        supported_item_types = [APP_LABEL + ".groupmember"]

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class GroupMemberListBlock(GroupMemberLayoutBlock):

    class Meta:
        classname = settings.OFFICEKIT_GROUP_MEMBER_LIST_BLOCK_CLASSNAME
        template = APP_LABEL + "/blocks/group_member_list_block.html"

    visuals = SwitchBlock(local_blocks=[
                ('figures', FigureBlock(user_configurable_content=False)),
                ('slideshow', SlideshowBlock(user_configurable_content=False))],
                default_block_name='figures',
                template=APP_LABEL + "/blocks/group_member_list_switch.html")

    show_visual_placeholders = blocks.BooleanBlock(default=False, required=False)
    hide_titles = blocks.BooleanBlock(default=False, required=False)


class GroupMemberLayoutBlockRegistry(BlockRegistry):

    # noinspection PyMethodMayBeStatic
    def should_include_entry_for_switch_block(self, identifier, entry, switch_block):
        return True

    # noinspection PyMethodMayBeStatic
    def instantiate_block(self, identifier, entry, switch_block):

        block_kwargs = dict(entry.block_kwargs)

        block_kwargs["user_configurable_content"] = False

        block = entry.block_type(*entry.block_args, **block_kwargs)
        block.set_name(identifier)

        return block


GROUP_MEMBER_LAYOUT_BLOCK_REGISTRY = GroupMemberLayoutBlockRegistry()
GROUP_MEMBER_LAYOUT_BLOCK_REGISTRY.define_procedures_in_caller_module("group_member_layout")

register_group_member_layout_block(APP_LABEL, "memberlist", GroupMemberListBlock, [], {}) # noqa


class GroupLayoutBlock(BaseContentLayoutBlock):

    class Meta:
        classname = settings.OFFICEKIT_GROUP_LAYOUT_BLOCK_CLASSNAME

        supported_item_types = [APP_LABEL + ".group"]

    def deconstruct(self):
        return blocks.Block.deconstruct(self)


class GroupListBlock(GroupLayoutBlock):

    class Meta:
        classname = settings.OFFICEKIT_GROUP_LIST_BLOCK_CLASSNAME
        member_layout_block_classname = settings.OFFICEKIT_GROUP_LIST_MEMBER_LAYOUT_BLOCK_CLASSNAME
        template = APP_LABEL + "/blocks/group_list_block.html"
        members_template = {
            APP_LABEL + "_memberlist": APP_LABEL + "/blocks/group_member_list_block.html"
        }

    show_group_headings = blocks.BooleanBlock(label="Show Group Headings", required=False, default=True)
    show_group_descriptions = blocks.BooleanBlock(label="Show Group Descriptions", required=False, default=True)

    member_layout = DynamicSwitchBlock(child_blocks_function_name=APP_LABEL + ".blocks.group_member_layout_block_choices",
                                       choice_label="Select")

    def __init__(self, *args, **kwargs):

        self.base_blocks['member_layout'].container_block = weakref.ref(self)

        super().__init__(*args, **kwargs)


class PersonNameBlock(blocks.StructBlock):
    class Meta:
        default = {"family_name": "", "given_names_and_initials": "", "identify_with": None}

    family_name = blocks.CharBlock(label="Family Name", default="", required=False)
    given_names_and_initials = blocks.CharBlock(label="Given Name(s) and Initial(s)", default="", required=False)

    identify_with = SnippetChooserBlock(APP_LABEL + ".person", label="Identify with", default=None, required=False)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)

    def json_from_group_member(self, group_member):

        if group_member is None:
            return None

        person = group_member.specific

        from .models import Person

        if person is None or not isinstance(person, Person):
            return None

        return dict([("family_name", person.family_name),
                     ("given_names_and_initials", person.given_names_and_initials),
                     ("identify_with", person.pk)])

    def value_from_group_member(self, group_member):

        if group_member is None:
            return None

        return self.to_python(self.json_from_group_member(group_member))


class OrganisationNameBlock(blocks.StructBlock):
    class Meta:
        default = {"name": "", "identify_with": None}

    name = blocks.CharBlock(label="Name", default="", required=False)
    identify_with = SnippetChooserBlock(APP_LABEL + ".organisation", label="Identify with", default=None, required=False)

    def deconstruct(self):
        return blocks.Block.deconstruct(self)

    def json_from_group_member(self, group_member):

        if group_member is None:
            return None

        organisation = group_member.specific

        from .models import Organisation

        if organisation is None or not isinstance(organisation, Organisation):
            return None

        return dict([("name", organisation.name),
                     ("identify_with", organisation.pk)])

    def value_from_group_member(self, group_member):

        if group_member is None:
            return None

        return self.to_python(self.json_from_group_member(group_member))


names_block = blocks.StreamBlock(local_blocks=[
    ("person", PersonNameBlock(label="Person")),
    ("organisation", OrganisationNameBlock(label="Organisation"))],
    required=False)

names_block.set_name("names")

NameListBlockValue = blocks.StructValue


class NameListBlock(blocks.StructBlock):

    class Meta:
        value_class = NameListBlockValue
        classname = settings.OFFICEKIT_NAME_LIST_BLOCK_CLASSNAME
        name_classname = settings.OFFICEKIT_NAME_LIST_BLOCK_NAME_CLASSNAME
        person_classname = settings.OFFICEKIT_NAME_LIST_BLOCK_PERSON_CLASSNAME
        organisation_classname = settings.OFFICEKIT_NAME_LIST_BLOCK_ORGANISATION_CLASSNAME
        container_element = "span"
        template = APP_LABEL + "/blocks/name_list_block.html"
        default = {"names": blocks.StreamValue(names_block, [], is_lazy=True)}
        required = False

    names = names_block

    def deconstruct(self):
        return blocks.Block.deconstruct(self)

    def json_from_group_members(self, group_members):

        from .models import Person, Organisation

        names = []
        result = {
            'names': names
        }

        for group_member in group_members:

            if group_member is None:
                continue

            identity = group_member.specific

            if identity is None:
                continue

            if isinstance(identity, Person):
                child_block = self.child_blocks['names'].child_blocks['person']
            elif isinstance(identity, Organisation):
                child_block = self.child_blocks['names'].child_blocks['organisation']
            else:
                child_block = None

            if child_block is None:
                continue

            identity = child_block.json_from_group_member(identity)

            names.append({'value': identity, 'type': child_block.name})

        return result

    def value_from_group_members(self, group_members):
        return self.to_python(self.json_from_group_members(group_members))
