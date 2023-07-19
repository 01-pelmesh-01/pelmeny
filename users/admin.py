#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from .models import CustomUser as User
#from .forms import CustomUserCreationForm as UserCreationForm
#from django.contrib import admin

#class UserAdmin(BaseUserAdmin):
#    add_form = UserCreationForm
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('email', 'first_name', 'last_name', 'is_bot_flag', 'password1', 'password2')}
#        ),
#    )

#admin.site.register(User, UserAdmin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , story
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (*UserAdmin.fieldsets,('доп. инфо:',{'fields':(
        'premium', 'like'
        )}))

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(story)
