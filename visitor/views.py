from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import visitor_model, staff_member_model, drink_model, visitor_detail_model, visitor_drink_model
from .serializers import VisitorSerializer, StaffMemberSerializer, DrinkSerializer, VisitorDetailSerializer, VisitorDrinkSerializer

# Create your views here.
class VisitorView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'),
            'mobile': request.data.get('mobile'), 
        }
        serializer = VisitorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffMemberView(APIView):
    
    def get(self, request, *args, **kwargs):
        staff_member = staff_member_model.objects.all()
        serializer = StaffMemberSerializer(staff_member, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DrinkView(APIView):
    
    def get(self, request, *args, **kwargs):
        drink = drink_model.objects.all()
        serializer = DrinkSerializer(drink, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisitorDetailView(APIView):

    def get(self, request, *args, **kwargs):
        visitor_detail = visitor_detail_model.objects.all()
        serializer = VisitorDetailSerializer(visitor_detail, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VisitorDrinkView(APIView):

    def get(self, request, *args, **kwargs):
        visitor_drink = visitor_drink_model.objects.all()
        serializer = VisitorDrinkSerializer(visitor_drink, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
