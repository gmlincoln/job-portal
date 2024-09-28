from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Custom_User)
class Custom_User_Display(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','user_type', 'email')
    search_fields = ('username', 'user_type')
    list_filter = ('user_type',)


@admin.register(Resume_Model)
class Resume_Model_Display(admin.ModelAdmin):
    list_display = ('user', 'designation', 'contact_number', 'date_of_birth',)
