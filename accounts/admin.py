from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CutomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "name",
        "is_staff"
    ]
    #the below two lines means, display the name field i
    # created in the add and change page in the admin
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("name",)}),)


admin.site.register(CustomUser, CutomUserAdmin)