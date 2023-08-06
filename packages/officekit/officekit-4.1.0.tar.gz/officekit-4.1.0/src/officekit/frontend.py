
from django.utils.deconstruct import deconstructible

from wagtail.admin.templatetags.wagtailadmin_tags import ellipsistrim

from wagtail_content_admin.content_admin import ContentAdmin
from wagtail_content_admin.frontend import ContentItemAction

from .models import Person, Organisation, GroupAssignment
from .permissions import group_assignment_permission_policy, group_member_permission_policy, group_permission_policy
from .apps import get_app_label


__all__ = ['group_assignment_admin', 'group_member_admin', 'group_admin',
           'GroupAssignmentAdmin', 'GroupMemberAdmin', 'GroupAdmin']


APP_LABEL = get_app_label()


class BaseAdmin(ContentAdmin): # noqa

    browser_order_by = ['identifier']

    template_name = None

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        return ''

    def render_preview(self, instance, **kwargs):
        inner = self.render_preview_inner(instance, **kwargs)
        title = ellipsistrim(self.title_for(instance), 60)
        return ('<figure class="content-item-preview"><span class="content-item-category-label">{}</span>'
                '{}<figcaption>{}</figcaption></figure>').format(
            self.get_verbose_name(instance=instance),
            inner,
            ellipsistrim(title, 60))

    def render_choice_inner(self, instance, **kwargs):
        return self.render_preview(instance, **kwargs)

    def configure_frontend_item(self, frontend_item, instance):
        frontend_item.model_verbose_name = self.get_verbose_name(instance=instance)
        frontend_item.title = self.title_for(instance)
        frontend_item.preview_html = self.render_preview(instance)

        edit = ContentItemAction('edit', title='Edit', url=self.edit_url_for(instance))
        frontend_item.add_action(edit)


@deconstructible
class GroupAssignmentAdmin(BaseAdmin):

    template_name = APP_LABEL + "/layouts/group_assignment.html"

    def __init__(self, add_url_specifiers=None):
        super().__init__()

        if add_url_specifiers is None:
            add_url_specifiers = []

        self.url_namespace = APP_LABEL
        self.url_prefix = 'group_assignment/'
        self.browser_url_name = 'group_assignment_index'
        self.chooser_url_name = 'group_assignment_chooser'
        self.chooser_results_url_name = 'group_assignment_chooser_results'
        self.content_item_chosen_name = 'group_assignment_content_item_chosen'

        self.permission_policy = group_assignment_permission_policy
        self.add_url_specifiers_ = list(add_url_specifiers)

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        member = instance.member.specific
        if isinstance(member, Person):
            return member.full_name
        elif isinstance(member, Organisation):
            return member.name

        return ''

    # noinspection PyMethodMayBeStatic
    def get_verbose_name(self, instance=None, plural=False):

        if instance is not None:

            member = instance.member.specific

            if isinstance(member, Person):
                return 'Person' if not plural else 'Persons'
            elif isinstance(member, Organisation):
                return 'Organisation' if not plural else 'Organisations'

        return 'Group Member' if not plural else 'Group Members'


group_assignment_admin = GroupAssignmentAdmin()


@deconstructible
class GroupMemberAdmin(BaseAdmin):

    template_name = APP_LABEL + "/layouts/group_member.html"

    def __init__(self, add_url_specifiers=None):
        super().__init__()

        if add_url_specifiers is None:
            add_url_specifiers = []

        self.url_namespace = APP_LABEL
        self.url_prefix = 'group_member/'
        self.browser_url_name = 'group_member_index'
        self.chooser_url_name = 'group_member_chooser'
        self.chooser_results_url_name = 'group_member_chooser_results'
        self.content_item_chosen_name = 'group_member_content_item_chosen'

        self.permission_policy = group_member_permission_policy
        self.add_url_specifiers_ = list(add_url_specifiers)

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):

        if isinstance(instance, Person):
            return instance.full_name
        elif isinstance(instance, Organisation):
            return instance.name

        return ''

    # noinspection PyMethodMayBeStatic
    def get_verbose_name(self, instance=None, plural=False):

        if instance is not None:

            instance = instance.specific

            if isinstance(instance, Person):
                return 'Person' if not plural else 'Persons'
            elif isinstance(instance, Organisation):
                return 'Organisation' if not plural else 'Organisations'

        return 'Group Member' if not plural else 'Group Members'

    def render_preview(self, instance, **kwargs):
        instance = instance.specific
        return super().render_preview(instance, **kwargs)


group_member_admin = GroupMemberAdmin()


@deconstructible
class GroupAdmin(BaseAdmin):

    def __init__(self, add_url_specifiers=None):
        super().__init__()

        if add_url_specifiers is None:
            add_url_specifiers = []

        self.url_namespace = APP_LABEL
        self.url_prefix = 'group/'
        self.browser_url_name = 'group_index'
        self.chooser_url_name = 'group_chooser'
        self.chooser_results_url_name = 'group_chooser_results'
        self.content_item_chosen_name = 'group_content_item_chosen'

        self.permission_policy = group_permission_policy
        self.add_url_specifiers_ = list(add_url_specifiers)

        self.group_assignment_admin = group_assignment_admin

    # noinspection PyMethodMayBeStatic
    def title_for(self, instance):
        return instance.name

    # noinspection PyMethodMayBeStatic
    def get_verbose_name(self, instance=None, plural=False):
        return 'Group' if not plural else 'Groups'


group_admin = GroupAdmin()

