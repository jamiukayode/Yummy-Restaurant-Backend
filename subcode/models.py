from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

#Sign Up table
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile = models.ImageField(upload_to="profile")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']




#food  table
class food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="food_images")

    def __str__(self):
        return self.name + " - " + str(self.price) + " - "  + " - " + str(self.description)



#Cart table
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #  if the user does not exist again delete cart from the database(CASCADE)
    food = models.ForeignKey(food, on_delete=models.CASCADE)
     #  if the user does not exist again cart will still be there(RESTRICT) if you use RESRICT
    qty = models.IntegerField(default=1)
    datecreated = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=1)
  

    def __str__(self):
        return self.user.email  + ' - ' + str(self.qty)


# Book a Table

class bookTable(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True,)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    no_of_people = models.IntegerField()
    message = models.TextField(max_length=350)
    datebooked = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.phone) 

    # def __str__(self):
    #     return f"{self.name} - {self.phone} - {self.date} - {self.time} - {self.no_of_people}"



# Send Message    
class Message(models.Model):
    name = models.CharField(max_length= 20)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=400)
    datemessage = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.email) 
