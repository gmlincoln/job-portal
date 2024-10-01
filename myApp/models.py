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
    
class DegreeType_Model(models.Model):

    DEGREE_TYPE = [
        ('ssc','SSC/Dakhil/Equivalent'),
        ('hsc','HSC'),
        ('diploma','Diploma'),
        ('bachelor',"Bachelor's Degree"),
        ('master',"Master's Degree"),
        ('phd',"Doctorate (PhD)"),
    ]

    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=200, blank=True)
    degree_level = models.CharField(choices=DEGREE_TYPE, max_length=100, null=True)

    def __str__(self):
        return self.name

class Institute_Model(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=80, blank=True)
    division = models.CharField(max_length=80, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(max_length=200, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True)

    def __str__(self):

        return f"{self.name}--{self.country}--{self.website}--{self.contact_number}"

class Field_of_Study_Model(models.Model):

    field_of_study = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.field_of_study}"



class Education_Model(models.Model):

    user = models.ForeignKey(Custom_User, null=True, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=200, null=True)
    degree_name = models.CharField(max_length=100, null=True)
    field_of_study = models.CharField(max_length=200, null=True)
    start_date = models.DateField(max_length=30, null=True)
    end_date = models.DateField(max_length=30, null=True)

    class Meta:
        unique_together = ('user','institute_name','degree_name')

    def __str__(self):
        return f"{self.user.username}--{self.institute_name}--{self.start_date}-{self.end_date}"
