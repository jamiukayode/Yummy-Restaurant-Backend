from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import food, User, Cart, bookTable, Message
from .serializer import foodSerializer, UserSerializer, LoginSerializer, cartSerializer, bookTableSerializer, MessageSerializer
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def signup(request):

    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        return Response(data=str(e), status=400)


@api_view(['GET'])
def allfoods(request):
    foods = food.objects.all()
    converted = foodSerializer(foods, many=True)
    return Response(data=converted.data, status=201)


@api_view(['POST'])
def login(request):

    try:
        serializer = LoginSerializer(request.data)
        user = serializer.checkuser(serializer.data)
        if user is None:
            return Response('Invalid credential', status=400)
        else:
            return Response(data=user, status=200)

    except BaseException as e:
        return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def addToCart(request, userId, foodId):
    if userId == "" or foodId == "":
        return Response(data="authentication failed", status=400)
    else:
        user = User.objects.filter(id=userId).first()
        Food = food.objects.filter(id=foodId).first()
        cart = Cart.objects.filter(user=user, food=Food).first()

        if cart is None:
            Cart.objects.create(
                user=user,
                food=Food
            )


            return Response(data="cart added succesfully", status=200)

        else:
            cart.total = cart.total + 1
            cart.qty = cart.qty + 1
            cart.save()

            return Response(data="cart added succesfully", status=200)


@api_view(['GET'])
def fecthCartByUser(request, id):
    user = User.objects.filter(id=id).first()
    allcarts = Cart.objects.filter(user = user).all()
    serializer = cartSerializer(allcarts, many=True)
    return Response(data=serializer.data, status= 200)


#book a table
@api_view(['POST'])
def BookTable(request):

    try:
        serializer = bookTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        return Response(data=str(e), status=400)
    


#send a message
@api_view(['POST'])
def SendMessage(request):

    try:
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        return Response(data=str(e), status=400)    