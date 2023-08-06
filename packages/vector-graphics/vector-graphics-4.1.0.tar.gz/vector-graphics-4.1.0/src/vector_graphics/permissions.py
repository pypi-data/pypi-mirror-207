from wagtail.core.permission_policies.base import OwnershipPermissionPolicy
from wagtail.core.permission_policies.collections import CollectionOwnershipPermissionPolicy

from .apps import get_app_label

APP_LABEL = get_app_label()

permission_policy = CollectionOwnershipPermissionPolicy(
    APP_LABEL + ".vectorgraphic",
    owner_field_name='created_by_user'
)

