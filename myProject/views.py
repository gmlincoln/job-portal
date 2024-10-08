from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from django.contrib import messages

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


from django.db import IntegrityError

from myApp.models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

import requests
import json


def homePage(req):
    
    user = req.user
    
    return render(req, 'common/index.html')


def loginPage(req):
    
    
    if req.method == 'POST':
        user_name = req.POST.get('username')
        password = req.POST.get('password')
        
        user = authenticate(req, username = user_name, password = password)        


        if not Custom_User.objects.filter(username = user_name).exists() and password:
            messages.warning(req, "Sorry! This user doesn't exist!")

        elif not user_name or not password:
            messages.warning(req, 'Both username and password required!')
            return render(req, 'common/login.html')
        
        
        elif user is not None:
            login(req, user)
            messages.success(req,'Login Successful!')
            return redirect('homePage')
        else:
            messages.warning(req,'Username or Password Wrong!')
    
    return render(req, 'common/login.html')

def logoutPage(req):
    logout(req)
    messages.success(req, 'Successfully logout!')
    return redirect('homePage')



def forgetPassword(req):
    if req.method == 'POST':
        user_email = req.POST.get('email')

        if Custom_User.objects.filter(email=user_email):
            captcha_token = req.POST.get('g-recaptcha-response')
            captcha_url = "https://www.google.com/recaptcha/api/siteverify"
            captcha_secret = "6LeVN1sqAAAAAC6mx8Kx6qZt250gK83z4bkT_f-H"

            captcha_data = {'secret':captcha_secret, 'response': captcha_token}
            captcha_server_response = requests.post(url=captcha_url, data=captcha_data)

            captcha_json = json.loads(captcha_server_response.text)

            if captcha_json['success'] == False:
                messages.error(req,'CAPTCHA validation failed. Please try again.')
                return render(req, 'common/forget-password.html')
            else:
                return redirect('passwordToken')
        
        else:
            messages.warning(req,'No user with this email exists.')
            return render(req, 'common/forget-password.html')

        
    return render(req, 'common/forget-password.html')


def passwordToken(req):

    

    return render(req, 'common/password-token.html')

def passwordReset(req):
    

    return render(req, 'common/password-reset.html')

def registerPage(req):
    
    if req.method == 'POST':
        first_name = req.POST.get('firstName')
        last_name = req.POST.get('lastName')
        username = req.POST.get('username')
        email = req.POST.get('email')
        user_type = req.POST.get('userType')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirmPassword')
    
        if not all([first_name, last_name, username, email, user_type, password, confirm_password]):
            messages.warning(req, 'All fields are required!')
            return render(req, 'common/register.html')
        
        try:
            EmailValidator(email)
        except ValidationError:
            messages.warning(req, 'Invalid email format!')
            return render(req, 'common/register.html')
        
        if password != confirm_password:
            messages.warning(req, 'Password not matched!')
            return render(req, 'common/register.html')


        if len(password) < 8:
            messages.warning(req, "Password at least 8 characters.")
            return render(req, 'common/register.html')
        
        if not any(num.isdigit() for num in password) or not any(char.isalpha() for char in password):
            messages.warning(req, 'Password must be contain numbers and letters.')
            return render(req, 'common/register.html')
        
        try:
            user = Custom_User.objects.create_user(
                first_name = first_name,
                last_name = last_name, 
                username = username,
                email = email,
                user_type = user_type,
                password = confirm_password
            )
            messages.success(req, 'Account create successfully! You can login your account now.')
            return redirect('loginPage')
        
        except IntegrityError:
            messages.warning(req, 'Username or Email already exists!')
            return render(req, 'common/register.html')
            

    return render(req, 'common/register.html')
      
        
def jobDetails(req):
    
    return render(req, 'common/job-details.html')

@login_required
def createResume(req):
    
    current_user = req.user

    resume = Resume_Model.objects.filter(user=current_user)

    if resume:
        messages.warning(req, 'Resume already exists!')
        return redirect('updateBasicInfo')
    else:
        if req.user.user_type == 'seeker':
        
            if req.method == 'POST':

                resume_instance, created = Resume_Model.objects.get_or_create(user=current_user)
                
                
                resume_instance.designation = req.POST.get('designation')
                resume_instance.date_of_birth = req.POST.get('dob')
                

                if resume_instance.profile_pic:
                    resume_instance.profile_pic = resume_instance.profile_pic
                else:
                    resume_instance.profile_pic = req.FILES.get('profile_picture')

                resume_instance.contact_number = req.POST.get('phone')
                resume_instance.address = req.POST.get('address')
                resume_instance.career_summary = req.POST.get('career_summary')

                resume_instance.save()

                current_user.first_name = req.POST.get('firstName')
                current_user.last_name = req.POST.get('lastName')
                current_user.email = req.POST.get('email')

                current_user.save()

                messages.success(req,'Basic info updated successfully!')

                return redirect('previewResume')

        else:
            messages.warning(req,'You are not authorized to access this page!')
            return redirect('createResume')

    return render(req, 'job_seeker/create-resume.html')


@login_required
def updateBasicInfo(req):
    
    current_user = req.user

    if req.user.user_type == 'seeker':
        
        if req.method == 'POST':

            resume_instance, created = Resume_Model.objects.get_or_create(user=current_user)
            
            
            resume_instance.designation = req.POST.get('designation')
            resume_instance.date_of_birth = req.POST.get('dob')
            

            if req.FILES.get('profile_picture'):
                resume_instance.profile_pic = req.FILES.get('profile_picture')
                
            else:
                resume_instance.profile_pic = resume_instance.profile_pic


            resume_instance.contact_number = req.POST.get('phone')
            resume_instance.address = req.POST.get('address')
            resume_instance.career_summary = req.POST.get('career_summary')

            resume_instance.save()

            current_user.first_name = req.POST.get('firstName')
            current_user.last_name = req.POST.get('lastName')
            current_user.email = req.POST.get('email')

            current_user.save()

            messages.success(req,'Basic info updated successfully!')

            return redirect('previewResume')

    else:
        messages.warning(req,'You are not authorized to access this page!')
        return redirect('createResume')

    basic_info = Resume_Model.objects.get(user=current_user)
    
    context = {
        'basic_info':basic_info
    }

    return render(req, 'job_seeker/create-resume.html', context)


@login_required
def previewResume(req):

    current_user = req.user

    resume_exists = Resume_Model.objects.filter(user=current_user).exists()

    if resume_exists:
        user_basic_info = Resume_Model.objects.get(user=current_user)
    else:
        messages.warning(req, "Sorry! You haven't created your resume yet")
        return redirect('createResume')
  
    education_info = Education_Model.objects.filter(user=current_user)
    experience_info = Experience.objects.filter(user=current_user)

    context = {
        'basic_info':user_basic_info,
        'education_info': education_info,
        'experience_info':experience_info,
    }
    
    return render(req, 'job_seeker/preview-resume.html',context)

@login_required
def addEducation(req):

    degree_info = DegreeType_Model.objects.all()
    institute_info = Institute_Model.objects.all()
    field_of_study = Field_of_Study_Model.objects.all()

    if req.user.user_type == 'seeker':
        try:
            if req.method == 'POST':
                degree_id = req.POST.get('degree_type')
                institute_text = req.POST.get('institution_text')
                institute_select_id = req.POST.get('institution_select')
                field_of_study_text = req.POST.get('field_of_study_text') 
                field_of_study_select_id = req.POST.get('field_of_study_select') 
                start_date  = req.POST.get('start_date')
                end_date = req.POST.get('end_date')
                
                
                if all([degree_id, institute_select_id or institute_text , field_of_study_text or field_of_study_select_id, start_date, end_date]):


                    education_instance = Education_Model.objects.create(user=req.user)
                    
                    degree_type_obj = DegreeType_Model.objects.get(id=degree_id)
                    education_instance.degree_name = degree_type_obj.degree_level


                    if institute_text:
                        education_instance.institute_name = institute_text

                    elif institute_select_id:
                        institute_select_obj = Institute_Model.objects.get(id=institute_select_id)
                        education_instance.institute_name = institute_select_obj.name

                    if field_of_study_text:
                        education_instance.field_of_study = field_of_study_text
                    
                    elif field_of_study_select_id:
                        field_of_study_select_obj = Field_of_Study_Model.objects.get(id=field_of_study_select_id)
                        education_instance.field_of_study = field_of_study_select_obj.field_of_study

                    education_instance.start_date = start_date
                    education_instance.end_date = end_date

                    education_instance.save()

                    messages.success(req, 'Education level added!')
                    return redirect('previewResume')
            

                else:
                    messages.warning(req,'All fields are required!')
                    return redirect('addEducation')
        except IntegrityError:
            messages.warning(req, 'Education level is already exists!')
            return redirect('addEducation')
            
            

    context = {
        'degree_info':degree_info,
        'institute_info':institute_info,
        'study_field': field_of_study,
    }

    return render(req, 'job_seeker/add-education.html', context)

@login_required
def updateEducation(req, edu_id):

    if req.user.user_type == 'seeker':
        edu_info = get_object_or_404(Education_Model, id = edu_id)


        if req.method == 'POST':
            

            edu_info.id = req.POST.get('edu_id')
            edu_info.degree_name = req.POST.get('degree_type')
            edu_info.institute_name = req.POST.get('institution_text')
            edu_info.field_of_study = req.POST.get('field_of_study_text')
            edu_info.start_date = req.POST.get('start_date')
            edu_info.end_date = req.POST.get('end_date')

            edu_info.save()
            return redirect('updateAll')

    context = {
        'education_info': edu_info,
    }    


    return render(req, 'job_seeker/update-education.html', context)

@login_required
def deleteEducation(req, edu_id):

    if req.user.user_type == 'seeker':
        edu_info = Education_Model.objects.filter(id=edu_id)
        edu_info.delete()
        return redirect('updateAll')

@login_required
def addExperience(req):
    current_user = req.user

    if current_user.user_type == 'seeker':
        if req.method == 'POST':
            experience_instance = Experience.objects.create(user=current_user)
            experience_instance.job_title = req.POST.get('job_title')
            experience_instance.company_name = req.POST.get('company_name')
            experience_instance.start_date = req.POST.get('start_date')
            experience_instance.end_date = req.POST.get('end_date')

            experience_instance.save()
            return redirect('updateAll')
    else:
        messages.warning(req, 'You are not authorized to access this page.')
        return redirect('homePage')
    
    return render(req, 'job_seeker/add-experience.html')

def updateExperience(req,exp_id):


    return HttpResponse('updateExperience')

def deleteExperience(req,exp_id):
    
    return HttpResponse('deleteExperience')

def addLanguage(req):

    return HttpResponse('AddSkill')
def updateLanguage(req):
    

    return HttpResponse('AddSkill')
def deleteLanguage(req):

    return HttpResponse('AddSkill')
def addSkill(req):

    return HttpResponse('AddSkill')
def updateSkill(req):

    return HttpResponse('AddSkill')
def deleteSkill(req):

    return HttpResponse('AddSkill')


def updateAll(req):

    current_user = req.user
    education_info = Education_Model.objects.filter(user = current_user)
    experience_info = Experience.objects.filter(user=current_user)

    context = {
        'education_info':education_info,
        'experience_info':experience_info,
    }

    return render(req, 'job_seeker/update-all.html', context)



@login_required
def classicLayout(req):

    return render(req, 'job_seeker/classic-layout.html')

@login_required
def modernLayout(req):

    return render(req, 'job_seeker/modern-layout.html')

@login_required
def creativeLayout(req):

    return render(req, 'job_seeker/creative-layout.html')


@login_required
def applyPage(req):

    current_user = req.user

    if current_user.user_type == 'seeker':
        return render(req, 'job_seeker/apply-page.html')
    
    elif current_user.user_type == 'recruiter':
        messages.warning(req,"You are not a job seeker!")
        return redirect("jobDetails")
    
@login_required
def appliedJobs(req):

    return render(req, 'job_seeker/applied-jobs.html')    
    
@login_required
def viewApplicationDetails(req):

    return render(req, 'job_seeker/view-application-details.html')
@login_required
def chatPage(req):

    return render(req, 'common/chat.html')


@login_required
def settingsPage(req):

    current_user = req.user

    user_info = Resume_Model.objects.filter(user = current_user)

    context = {
        'user_info' : user_info
    } 

    return render(req, 'common/settings.html', context)



@login_required
def changePassword(req):
    
    current_user = req.user
    
    if req.method == 'POST':
        old_password = req.POST.get('oldPassword')
        new_password = req.POST.get('newPassword')
        repeat_password = req.POST.get('repeatNewPassword')
        
        if all([old_password, new_password, repeat_password]):
            
            if check_password(old_password, current_user.password):
            
                if len(new_password) >=8 and len(repeat_password) >= 8:
                    
                    if new_password == repeat_password:
                    
                        current_user.set_password(new_password)
                        current_user.save()
                        
                        #To prevent logout
                        update_session_auth_hash(req, current_user)
                        
                        messages.success(req, 'Password successfully changed!')
                        
                        return redirect('homePage')
                    
                    else:
                        messages.warning(req, 'New password and repeat password is not match!')
                        return render(req, 'common/settings.html')
                        
                else:
                    messages.warning(req,'Password at least 8 characters!')
                    return render(req, 'common/settings.html')
                    
    
            else:
                messages.warning(req, 'Old password is incorrect!')
                return render(req, 'common/settings.html')
                
        else:
            messages.warning(req, 'All password fields are required!')
            return render(req, 'common/settings.html')
        
        
        
    return render(req, 'common/settings.html')





@login_required
def dashboardPage(req):

    return render(req,'job_creator/index.html')





#https://github.com/rajeshdiu/Job-Portal-Class-Practice/blob/main/myProject/myProject/views.py

#bangladesh1212