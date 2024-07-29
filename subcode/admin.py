from django.contrib import admin
from .models import User, food, Cart, bookTable, Message

# Register your models here.

admin.site.register(User)
admin.site.register(food)
admin.site.register(Cart)
admin.site.register(bookTable)
admin.site.register(Message)
