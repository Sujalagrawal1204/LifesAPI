from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(['GET'])
def check(request,id):
    try:
        driver = Driver.objects.get(userId=id)
        serializer = DriverSerializer(driver)
        return Response({'status':200,'message':serializer.data})
    except Driver.DoesNotExist:
        try:
            fleat = FleatOwner.objects.get(userId = id)
            fleatserialize = FleatSerializer(fleat)
            return Response({'status':201,'message':fleatserialize.data})
        except FleatOwner.DoesNotExist:
            try:
                driverofFleat = DriverOfFleat.objects.get(userId=id)
                driverofFleatSer = DriverOfFleatSerializer(driverofFleat)
                return Response({'status':201,'message':driverofFleatSer.data})
            except ObjectDoesNotExist:
                return Response({'status':400,'message':"First Time Arrived"})


class DriverAPI(APIView):
    def get(self,request):
        try:
            drivers = Driver.objects.all()
            serializer = DriverSerializer(drivers,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
    
    @api_view(['PATCH'])
    def updateBusy(request,id):
        try:
            driver = Driver.objects.get(pk=id)
            data = request.data
            serializer = DriverSerializer(driver,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'message':"Updated Successfully"})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
    # @api_view(['PATCH'])
    # def updateFirst(request,id):
    #     driver = Driver.objects.get(pk=id)
    #     data = request.data
    #     serializer = DriverSerializer(driver,data=data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status':200,'message':"Updated Successfully"})
    #     return Response({'status':400,'message':"Unsuccessfully"})
    
    @api_view(['GET'])
    def getDriver(request,id):
        try:
            driver = Driver.objects.get(userId=id)
            print(driver)
            serializer = DriverSerializer(driver)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})  
    
    def post(self,request):
        try:
            data = request.data 
            serializer = DriverSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'message':"Added Successfully"})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
    def patch(self,request):
        try:
            data = request.data
            # return Response({'data':data})
            driver = Driver.objects.get(pk=data['id'])
            serializer = DriverSerializer(driver,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'message':"Updated Successfully"})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
class AmbulanceAPI(APIView):
    def get(self,request):
        try:
            ambulances = Ambulance.objects.all()
            serializer = AmbulanceSerializer(ambulances,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
    
    def post(self,request):
        try:
            data = request.data 
            serializer = AmbulanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':serializer.data})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})

    @api_view(['PATCH'])    
    def updateBusy(request,id):
        try:
            ambulance = Ambulance.objects.get(pk=id)
            data = request.data 
            serializer = AmbulanceSerializer(ambulance,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'message':"Updated Successfully"})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
    @api_view(['PATCH'])    
    def updateFirst(request,id):
        try:
            ambulance = Ambulance.objects.get(pk=id)
            data = request.data 
            serializer = AmbulanceSerializer(ambulance,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':200,'message':"Updated Successfully"})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
    
    @api_view(['GET'])
    def ambulanceId(request,id):
        try:
            ambulance = Ambulance.objects.filter(fleatId=id)
            # print(ambulance)
            serializer = AmbulanceSerializer(ambulance,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
        
class DriverOfFleatAPI(APIView):
    def get(self,request):
        try:
            drivers = DriverOfFleat.objects.all()
            serializer = DriverOfFleatSerializer(drivers,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"}) 
    
    def post(self,request):
        try:
            driver = request.data
            serializer = DriverOfFleatSerializer(data=driver)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':serializer.data})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
    
    @api_view(['GET'])
    def getByID(request,id):
        try:
            driver = DriverOfFleat.objects.get(pk=id)
            serializer = DriverOfFleatSerializer(driver)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
    
    @api_view(['POST'])
    def setAmbulance(request):
        try:
            serializer = DriverOfFleatSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':serializer.data})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
    @api_view(['POST'])
    def setFleat(request):
        try:
            serializer = DriverOfFleatSerializer(data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':serializer.data})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
    @api_view(['POST'])
    def AmbulanceAndFleatID(request):
        try:
            data = request.data
            print(request.data)
            user = User.objects.get(username=data['username'])
            fleat = FleatOwner.objects.get(userId=user.id) 
            fleats = FleatSerializer(fleat)
            print(fleat)
            ambulance = Ambulance.objects.get(regNumber=data['regNumber'])
            ambulances = AmbulanceSerializer(ambulance)
            return Response({'status':201,'data':{'fleatOwner':fleats.data},'ambulance':ambulances.data})
        except:
            return Response({'status':400,"message":"Error"})
        
class RegisterAPI(APIView):
    def post(self,request):
        try:
            data = request.data 
            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':'Successfully Registered'})
            return Response({'status':400,'data':"Error"})
        except:
            return Response({'status':400,"message":"Error"})
    
    def get(self,request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
    
    def patch(self,request):
        try:
            data = request.data
            user = User.objects.get(username=data['username'])
            serializer = UserSerializer(user,data=data,partial=True)
            if serializer.is_valid():
                return Response({'status':200,'message':'Updated Successfully'})
            return Response({'status':400,'message':"Unsuccessfully"})
        except:
            return Response({'status':400,"message":"Error"})
        
class LoginAPI(APIView):
    def post(self,request):
        try:
            data = request.data 
            serializer = LoginSerializer(data = data)
            if not serializer.is_valid():
                return Response({'status':False,'message':serializer.errors})
            serializer.save()

            user = authenticate(username=data['username'],password=data['password'])
            using = UserSerializer(user)
            if not user:
                return Response({'status':False,'message':'Invalid '})
            return Response({'status':200,'message':'User LoggedIn','user':using.data})
        except:
            return Response({'status':400,"message":"Error"})
        
class UserAPI(APIView):
    def get(self,request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
    
    # @api_view(['PATCH'])
    # def firsAppeared(request,id):
    #     user = User.objects.get(pk=id)
    #     data = request.data
    #     serializer = UserSerializer(user,data=data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status':200,'message':serializer.data})
    #     return Response({'status':400,'message':"Unsuccessfully"})


    
class FleatAPI(APIView):
    def get(self,request):
        try:
            fleats = FleatOwner.objects.all()
            serializer = FleatSerializer(fleats,many=True)
            return Response({'status':200,'data':serializer.data})
        except:
            return Response({'status':400,"message":"Error"})
        
    def post(self,request):
        try:
            data = request.data 
            serializer = FleatSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':201,'data':serializer.data})
            return Response({'status':400,'message':'Unsuccessful'})
        except:
            return Response({'status':400,"message":"Error"})
    

