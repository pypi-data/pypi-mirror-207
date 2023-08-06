from django.conf.urls import include
from django.urls import re_path

from wagtail import hooks

from .viewsets.chooser import create_group_member_viewset
from . import admin_urls

from .apps import get_app_label

APP_LABEL = get_app_label()


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^' + get_app_label() + '/', include(admin_urls, namespace=get_app_label())),
    ]


@hooks.register("register_admin_viewset")
def register_viewsets():
    return [create_group_member_viewset("group_member", APP_LABEL, "GenericGroupMember")]
