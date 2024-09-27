from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Custom_User(AbstractUser):
    
    USER = [
        ('seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter')
        
    ]
    
    user_type = models.CharField(choices=USER, max_length=40, null=True)
    
    
    def __str__(self):
        
        return f"{self.username}--{self.first_name} {self.last_name}"
    

class Resume_Model(models.Model):

    user = models.ForeignKey(Custom_User, null=True, on_delete=models.CASCADE)

    designation = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='Media/Profile_Pic')
    contact_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=150, null=True)
    career_summary = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f"{self.user.username}--{self.designation}--{self.contact_number}"
    

