from django.contrib import admin
from users.models import *

admin.site.register(Group)
admin.site.register(Permission)
admin.site.register(UserProfile)
admin.site.register(UserGroup)
admin.site.register(GroupPermission)
admin.site.register(UserPermission)
admin.site.register(UserExtendInfo)