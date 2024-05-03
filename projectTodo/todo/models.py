from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)    
    
    def __str__(self):
        return self.username

        
class task(models.Model):
    def get_default_username():
        # Assuming there's only one Register instance
        register_instance = Register.objects.first()
        return register_instance.username
    username = models.CharField(max_length=50, default=get_default_username)
    taskTitle = models.CharField(max_length=50)
    taskDesc = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)