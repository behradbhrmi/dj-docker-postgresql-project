from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username', )
