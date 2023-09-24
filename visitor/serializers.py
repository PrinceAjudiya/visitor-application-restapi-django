from rest_framework import serializers
from .models import visitor_model, staff_member_model, drink_model, visitor_detail_model, visitor_drink_model

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = visitor_model
        fields = ["name", "email", "mobile", "timestamp"]

class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = staff_member_model
        fields = ["name", "email", "mobile", "image"]

class DrinkSerializer(serializers.ModelSerializer):
    serve_member_name = serializers.CharField(source= 'serve_member_name.name')
    class Meta:
        model = drink_model
        fields = ['name', 'serve_member_name']

class VisitorDetailSerializer(serializers.ModelSerializer):
    staff_member_name = serializers.CharField(source='staff_member_name.name', read_only=True)
    visitor_name = serializers.CharField(source= 'visitor_name.name', read_only=True)
    class Meta:
        model = visitor_detail_model
        fields = ["staff_member_name", "visitor_name", "reason", "state", "timestamp"]

class VisitorDrinkSerializer(serializers.ModelSerializer):
    visitor_name = serializers.CharField(source= 'visitor_name.name')
    drink_name = serializers.CharField(source= 'drink_name.name')
    class Meta:
        model = visitor_drink_model
        fields = ["visitor_name", "drink_name", "state", "timestamp"]
