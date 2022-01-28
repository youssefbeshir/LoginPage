from rest_framework import serializers
from .models import proctor

from django.contrib.auth.hashers import make_password 

class UserRegistiration(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only  =True)
    class Meta:
        model = proctor
        fields= ['ID', 'first_name','last_name','email','password','password2','ExamCenterID', 'dob']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    
    def save(self):
        proc = proctor(
            
            ID = self.validated_data['ID'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email'],
            ExamCenterID = self.validated_data['ExamCenterID'],
            dob = self.validated_data['dob'],
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        
        if password != password2:
            raise serializers.ValidationError({"password":"Passwords Should Match!"})
        
        proc.password = make_password('password')
        proc.save()
        return proc
    