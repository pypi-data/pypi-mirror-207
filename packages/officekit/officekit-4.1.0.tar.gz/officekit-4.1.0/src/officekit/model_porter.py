
from media_catalogue.model_porter import media_chooser_value

from model_porter.config import ModelPorterConfig

from .models import GroupAssignment


def define_group_assignments(*, assignments, context):

    group = context.get_variable(context.INSTANCE_VARIABLE)

    result = []

    for assign in assignments:

        is_active, member_ref, description, visual, link = assign

        member = context.get_instance(member_ref, None)
        visual = media_chooser_value(items=visual, context=context)

        assign = GroupAssignment()
        assign.active = is_active
        assign.group_id = group.id
        assign.member_id = member.id
        assign.short_description = description
        assign.visual = visual

        result.append(assign)

    return result


class OfficeKitConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(OfficeKitConfig, self).__init__(app_label, module)
        self.register_function_action(define_group_assignments, context_argument='context')
