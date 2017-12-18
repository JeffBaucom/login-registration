from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters'

        if len(postData['lastName']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'

        if len(postData['email']) < 1:
            errors['email'] = 'Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email'

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        elif postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Password confirmation must match'

        if not errors:
            firstName = postData['firstName']
            lastName = postData['lastName']
            email = postData['email']
            try:
                user = User.objects.get(email=email)
                errors['email'] = 'Email has alerady been registered'
            except:
                password = postData['password']
                hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                # Return User Object
                return User.objects.create(first_name=firstName, last_name=lastName, email=email, password=hash1)
        return errors

    def login_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = 'Email is required'
        if len(postData['password']) < 1:
            errors['password'] = 'Password is required'
        if not errors:
            email = postData['email']
            password = postData['password']
            try:
                user = User.objects.get(email=email)
            except:
                error['password'] = 'Incorrect email or password'
            check = bcrypt.checkpw(password.encode(), user.password.encode())
            if not check: 
                error['password'] = 'Incorrect email or password'
            else:
                # Return User Object
                return user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
