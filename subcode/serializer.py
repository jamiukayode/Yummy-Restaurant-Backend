from rest_framework import serializers
from .models import food, User, Cart, bookTable, Message
from django.contrib.auth import authenticate


class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        # fields = ["id", "name",]
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ['profile']


# 'create' is an in-built function given to us by django but it is not s art enough to encrypte password. that is the reason we write the code below to encrypte Our users's password.


    def create(self, data):
        User.objects.create_user(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password'],
            profile=data['profile'],
        )
        return data


# function for login users
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def checkuser(self, data):
        user = authenticate(email=data['email'], password=data['password'])

        if user is None:
            return None
        else:
            id = getattr(user, 'id')
        return id

#cart
class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        depth = 1


#bookTable      
class bookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model =bookTable
        fields = "__all__"




#send Message
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"        