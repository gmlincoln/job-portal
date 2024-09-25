from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib import messages

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from django.db import IntegrityError

from myApp.models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def homePage(req):
    
    user = req.user
    
    return render(req, 'common/index.html')


def loginPage(req):
    
    
    if req.method == 'POST':
        user_name = req.POST.get('username')
        password = req.POST.get('password')
        
        if not user_name or not password:
            messages.warning(req, 'Both username and password required!')
            return render(req, 'common/login.html')
        
        user = authenticate(req, username = user_name, password = password)
        
        if user is not None:
            login(req, user)
            messages.success(req,'Login Successful!')
            return redirect('homePage')
        else:
            messages.warning(req,'Username or Password Wrong!')
    
    return render(req, 'common/login.html')

def logoutPage(req):
    logout(req)
    messages.success(req, 'Successfully logout!')
    return redirect('loginPage')


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
    return render(req, 'job_seeker/create-resume.html')

@login_required
def previewResume(req):

    return render(req, 'job_seeker/preview-resume.html')

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