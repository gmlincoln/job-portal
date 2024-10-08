"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('jobDetails/', jobDetails, name='jobDetails'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('forgetPassword/', forgetPassword, name='forgetPassword'),
    path('passwordToken/', passwordToken, name='passwordToken'),
    path('passwordReset/', passwordReset, name='passwordReset'),
    path('createResume/', createResume, name='createResume'),
    path('updateBasicInfo/', updateBasicInfo, name='updateBasicInfo'),
    path('previewResume/', previewResume, name='previewResume'),
    path('settingsPage/', settingsPage, name='settingsPage'),
    path('addEducation/', addEducation, name='addEducation'),
    path('classicLayout/', classicLayout, name='classicLayout'),
    path('modernLayout/', modernLayout, name='modernLayout'),
    path('creativeLayout/', creativeLayout, name='creativeLayout'),
    path('applyPage/', applyPage, name='applyPage'),
    path('appliedJobs/', appliedJobs, name='appliedJobs'),
    path('viewApplicationDetails/', viewApplicationDetails, name='viewApplicationDetails'),
    path('changePassword/', changePassword, name='changePassword'),
    path('dashboardPage/', dashboardPage, name='dashboardPage'),
    path('updateEducation/<int:edu_id>', updateEducation, name='updateEducation'),
    path('deleteEducation/<int:edu_id>', deleteEducation, name='deleteEducation'),
    path('addExperience/', addExperience, name='addExperience'),
    path('updateExperience/<int:exp_id>', updateExperience, name='updateExperience'),
    path('deleteExperience/<int:exp_id>', deleteExperience, name='deleteExperience'),
    path('addLanguage/', addLanguage, name='addLanguage'),
    path('updateLanguage/', updateLanguage, name='updateLanguage'),
    path('deleteLanguage/', deleteLanguage, name='deleteLanguage'),
    path('addSkill/', addSkill, name='addSkill'),
    path('updateSkill/', updateSkill, name='updateSkill'),
    path('deleteSkill/', deleteSkill, name='deleteSkill'),    
    path('updateAll/', updateAll, name='updateAll'),    
    path('chatPage/', chatPage, name='chatPage'),    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)