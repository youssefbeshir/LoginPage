from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserRegistiration
# Create your views here.

@api_view(['POST'])
def register(request):
    """API That registers users in the database

    Args:
        request ([type]): [description]
    """
    if request.method == 'POST':
        serializer = UserRegistiration(data = request.data)
        data = {}
        if serializer.is_valid():
            proctor = serializer.save()
            data['response'] = "Successfully registered a new user"
            data["email"] = proctor.email
            data["ID"] = proctor.ID 
        else:
            data = serializer.errors
            
        return Response(data)
    
