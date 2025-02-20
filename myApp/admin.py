from django.contrib import admin

from myApp.models import Custom_User, DegreeType_Model, Education_Model, Experience, Field_of_Study_Model, Institute_Model, Resume_Model



# Register your models here.


@admin.register(Custom_User)
class Custom_User_Display(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','user_type', 'email')
    search_fields = ('username', 'user_type')
    list_filter = ('user_type',)

@admin.register(Resume_Model)
class Resume_Model_Display(admin.ModelAdmin):
    list_display = ('user', 'designation', 'contact_number', 'date_of_birth',)
    search_fields = ('user__username','designation')
    list_filter = ('designation',)

@admin.register(DegreeType_Model)
class DegreeType_Model_Display(admin.ModelAdmin):
    list_display = ('name','degree_level','description')


@admin.register(Institute_Model)
class Institute_Model_Display(admin.ModelAdmin):

    list_display = ('name','country','established_year','email','contact_number')
    search_fields = ('name','country')
    list_filter = ('country','established_year','division')

@admin.register(Field_of_Study_Model)
class Field_of_Study_Model_Display(admin.ModelAdmin):
    list_display = ('id', 'field_of_study')



@admin.register(Education_Model)
class Education_Model_Display(admin.ModelAdmin):
    list_display = ('user','institute_name','start_date', 'end_date')

@admin.register(Experience)
class Experience_Model_Display(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'company_name')
    search_fields = ('user', 'job_title')
