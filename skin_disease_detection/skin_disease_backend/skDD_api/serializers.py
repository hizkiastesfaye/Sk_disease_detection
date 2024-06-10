from rest_framework import serializers
from .models import Profile, DataHistory

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class DataHistory_serializer(serializers.ModelSerializer):
    class Meta:
        model = DataHistory
        fields = '__all__'