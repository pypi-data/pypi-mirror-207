
from wagtail.permission_policies.collections import CollectionOwnershipPermissionPolicy
from threedee.models import ParaviewWebGLModel


permission_policy = CollectionOwnershipPermissionPolicy(
    ParaviewWebGLModel,
    auth_model=ParaviewWebGLModel,
    owner_field_name='created_by_user'
)
