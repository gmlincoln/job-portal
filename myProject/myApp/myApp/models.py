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