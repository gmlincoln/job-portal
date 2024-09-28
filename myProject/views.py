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

            current_user.firstname = req.POST.get('first_name')
            current_user.lastname = req.POST.get('last_name')
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
            

            if resume_instance.profile_pic:
                resume_instance.profile_pic = resume_instance.profile_pic
            else:
                resume_instance.profile_pic = req.FILES.get('profile_picture')

            resume_instance.contact_number = req.POST.get('phone')
            resume_instance.address = req.POST.get('address')
            resume_instance.career_summary = req.POST.get('career_summary')

            resume_instance.save()

            current_user.firstname = req.POST.get('first_name')
            current_user.lastname = req.POST.get('last_name')
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

    try:
        user_basic_info = get_object_or_404(Resume_Model,user=current_user) 
    
    except Http404:
        messages.warning(req, "Sorry! You haven't created your resume yet")
        return redirect('createResume')


    
    context = {
        'basic_info':user_basic_info,
    }
    
    return render(req, 'job_seeker/preview-resume.html',context)

@login_required
def appliedJobs(req):

    return render(req, 'job_seeker/applied-jobs.html')

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

    return render(req, 'job_seeker/apply-page.html')

@login_required
def settingsPage(req):

    return render(req, 'common/settings.html')



@login_required
def changePassword(req):
    
    current_user = req.user
    
    if req.method == 'POST':
        old_password = req.POST.get('oldPassword')
        new_password = req.POST.get('newPassword')
        repeat_password = req.POST.get('repeatNewPassword')
        
        if check_password(old_password, current_user.password):
            
            if len(new_password) >=8 and len(repeat_password) >= 8:
                
                if new_password == repeat_password:
                
                    current_user.set_password(new_password)
                    current_user.save()
                    
                    #To prevent logout
                    update_session_auth_hash(req, current_user)
                    
                    messages.success(req, 'Password successfully changed!')
                    
                    return redirect('previewResume')
                
                else:
                    messages.warning(req, 'New password and repeat password is not match!')
            else:
                messages.warning(req,'Password at least 8 characters!')
    
        else:
            messages.warning(req, 'Old password is incorrect!')
        
        
        
    return render(req, 'common/settings.html')



#https://github.com/rajeshdiu/Job-Portal-Class-Practice/blob/main/myProject/myProject/views.py

#bangladesh1212