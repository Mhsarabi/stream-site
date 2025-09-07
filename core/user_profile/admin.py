from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display=["user_name","email","is_superuser","is_active",'is_verified']
    list_filter=["user_name","email","is_superuser","is_active",'is_verified']
    search_fields=("email","user_name")
    ordering=('email',"user_name")
    add_form = RegisterUserForm
    fieldsets=(
        ("personal_data",{
            "fields":(
                "user_name","email","password"
            )
        }),
        ("group_permission",{
            "fields":(
                "groups","user_permissions"
            )
        }),
        ("important_date",{
            "fields":(
                "last_login",
            )
        }),
        ("permission",{
            "fields":(
                'is_staff','is_active',"is_superuser",'is_verified'
            )
        })  
    )
    add_fieldsets=(
        ("personal_date",{
            "fields":(
                "user_name","email","password1","password2","is_staff","is_active","is_superuser"
            )
        }),
    )
admin.site.register(User,CustomUserAdmin)
admin.site.site_header="streaming site admin"