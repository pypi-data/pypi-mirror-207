
from .frontend import group_assignment_admin, group_member_admin, group_admin
from .apps import get_app_label

app_name = get_app_label()

urlpatterns = group_assignment_admin.create_admin_urls() + \
              group_member_admin.create_admin_urls() + group_admin.create_admin_urls() + [
]
