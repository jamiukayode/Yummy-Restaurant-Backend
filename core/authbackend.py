from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class EmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, email = None, password = None ):  
        userModel = get_user_model()

        try:
            user  = userModel.objects.get(email = email)
        except userModel.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        else:
            return None