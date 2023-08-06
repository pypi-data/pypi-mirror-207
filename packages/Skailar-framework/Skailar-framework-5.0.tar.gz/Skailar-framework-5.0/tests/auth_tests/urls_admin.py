"""
Test URLs for auth admins.
"""

from skailar.contrib import admin
from skailar.contrib.auth.admin import GroupAdmin, UserAdmin
from skailar.contrib.auth.models import Group, User
from skailar.contrib.auth.urls import urlpatterns
from skailar.urls import path

# Create a silo'd admin site for just the user/group admins.
site = admin.AdminSite(name="auth_test_admin")
site.register(User, UserAdmin)
site.register(Group, GroupAdmin)

urlpatterns += [
    path("admin/", site.urls),
]
