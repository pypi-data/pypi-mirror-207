from django import template
from django.templatetags.static import static

from ..apps import get_app_label
from ..models import GroupAssignment, GroupMember, Organisation, Person

APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(name="cast_group_member", takes_context=True)
def cast_group_member_tag(context, value):

    group_assignment = None
    group = None

    group_member = None
    person = None
    organisation = None

    if isinstance(value, GroupAssignment):
        group_assignment = value
    elif isinstance(value, GroupMember):
        group_member = value

        if isinstance(value.specific, Person):
            person = value.specific
        elif isinstance(value.specific, Organisation):
            organisation = value.specific

    elif isinstance(value, Person):
        group_member = value
        person = value.specific
    elif isinstance(value, Organisation):
        group_member = value
        organisation = value.specific

    context['group_assignment'] = group_assignment
    context['group'] = group
    context['group_member'] = group_member
    context['person'] = person
    context['organisation'] = organisation

    return ''


def gather_style_sheets():

    urls = [# static(APP_LABEL + '/css/group_block.css'),
            # static(APP_LABEL + '/css/group_layout.css')
           ]

    return urls


def gather_scripts():

    urls = []

    return urls


SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'


@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="officekit_support")
def officekit_support_tag(*, container_element, is_admin_page=False):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'stylesheets': gather_style_sheets(),
        'scripts': gather_scripts()
    }

    return result
