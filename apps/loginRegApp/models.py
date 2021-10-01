from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name'])== 0:
            errors['first_name'] ='First Name required!'

        if len(postData['last_name'])== 0:
            errors['last_name'] = 'Last Name required!'

        if len(postData['email'])== 0:
            errors['email'] = 'Email required!'
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        elif check:
            errors['email'] = "Email address is already registered."
            
        if len(postData['password'])== 0:
            errors['password'] = 'Password required!'

        if postData['password']!= postData['confirm_password']:
            errors['match']= 'Passwords do not match!'
        return errors
        
    def login_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email = postData['email'])
        if len(postData['email'])== 0:
            errors['email'] = 'Email required!'
        elif len(existing_users)== 0:
            errors['does_not_exist']= "Email not found" #"Please enter a valid email and password"
        elif len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long!'
        elif not bcrypt.checkpw(postData['password'].encode(), existing_users[0].password.encode()):
            errors['mismatch']= "Please enter a valid email and password"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # OTM with comments 
    # OTM with messages