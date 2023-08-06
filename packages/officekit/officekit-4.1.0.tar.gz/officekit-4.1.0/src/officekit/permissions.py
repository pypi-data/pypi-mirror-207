# -*- coding: utf-8 -*-

from django.utils.translation import gettext_lazy as _
from wagtail.permission_policies.base import ModelPermissionPolicy

from .apps import get_app_label

__all__ = ['group_assignment_permission_policy', 'group_member_permission_policy', 'group_permission_policy']

APP_LABEL = get_app_label()

group_assignment_permission_policy = ModelPermissionPolicy(
    APP_LABEL + ".groupassignment"
)

group_member_permission_policy = ModelPermissionPolicy(
    APP_LABEL + ".groupmember"
)

group_permission_policy = ModelPermissionPolicy(
    APP_LABEL + ".group"
)


GROUP_MEMBER_PERMISSION_TYPES = [
    ('add', _("Add"), _("Add/edit group members you own")),
    ('edit', _("Edit"), _("Edit any group member")),
]

GROUP_MEMBER_PERMISSION_TYPE_CHOICES = [
    (identifier, long_label)
    for identifier, short_label, long_label in GROUP_MEMBER_PERMISSION_TYPES
]


GROUP_PERMISSION_TYPES = [
    ('add', _("Add"), _("Add/edit groups you own")),
    ('edit', _("Edit"), _("Edit any group")),
]

GROUP_PERMISSION_TYPE_CHOICES = [
    (identifier, long_label)
    for identifier, _, long_label in GROUP_PERMISSION_TYPES
]
