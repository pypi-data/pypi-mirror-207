
from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


from wagtail.coreutils import resolve_model_string
from wagtail.admin.widgets.chooser import BaseChooser, BaseChooserAdapter
from wagtail.telepath import register


from .apps import get_app_label

__all__ = ['BaseGroupMemberChooser']

APP_LABEL = get_app_label()


class BaseGroupMemberChooser(BaseChooser):

    model = APP_LABEL + ".groupmember" # noqa
    display_title_key = "string"
    icon = "snippet"
    classname = "group-member-chooser"

    choose_one_text = _('Choose a group member')
    choose_another_text = _('Choose another group member')
    link_to_chosen_text = _('Edit this group member')

    def __init__(self, specific_models=None, **kwargs):

        if specific_models is None:
            specific_models = []

        self.specific_models = tuple(specific_models or [APP_LABEL + ".groupmember"])

        super().__init__(**kwargs)

        if self.specific_model_classes:
            # noinspection PyProtectedMember
            models = ', '.join([model._meta.verbose_name.title() for model in self.specific_model_classes])
            if models:
                self.choose_one_text += ' (' + models + ')'

    @cached_property
    def specific_model_classes(self):
        return tuple([resolve_model_string(specific_model) for specific_model in self.specific_models])

    def get_instance(self, value):
        """
        Given a value passed to this widget for rendering (which may be None, an id, or a model
        instance), return a model instance or None
        """
        if value is None:
            return None
        elif isinstance(value, self.model_class):
            return value.specific
        else:  # assume instance ID
            result = self.model_class.objects.get(pk=value) # noqa
            result = result.specific if result is not None else result
            return result


class BaseGroupMemberChooserAdapter(BaseChooserAdapter):
    js_constructor = APP_LABEL + ".widgets.BaseGroupMemberChooser"

    @cached_property
    def media(self):
        return super().media + forms.Media(
            js=[
            ]
        )


register(BaseGroupMemberChooserAdapter(), BaseGroupMemberChooser)
