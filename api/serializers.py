from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        # fields = ['id','username','first_name','last_name','email']

# class CustomUserSerializer(UserSerializer):
#     first = serializers.BooleanField()
#     # if first == False:
#     #     first = True
#     class Meta(UserSerializer.Meta):
#         fields = UserSerializer.Meta.fields + ['first']

class DriverSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Driver
        fields = ['id','regNumber','carModel','busy','type','userId','phone']

class FleatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleatOwner
        fields = '__all__'

class AmbulanceSerializer(serializers.ModelSerializer):
    # fleatId = FleatSerializer()
    class Meta:
        model = Ambulance
        fields = ['id','regNumber','carModel','busy','type','fleatId']
        depth = 1


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username is Taken")
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError("Email is Already Registered")
            
        return data

    def create(request,validated_data):
        user = User.objects.create(first_name = validated_data['first_name'],last_name = validated_data['last_name'],username = validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self,validated_data):
        user = User.objects.get(username = validated_data['username'])
        return user
    
class DriverOfFleatSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverOfFleat
        fields = '__all__'