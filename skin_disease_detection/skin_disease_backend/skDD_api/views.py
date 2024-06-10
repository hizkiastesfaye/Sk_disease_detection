from django.shortcuts import render
from rest_framework import generics
from .models import Profile, DataHistory
from .serializers import Profile_serializer, DataHistory_serializer
# Create your views here.

class ProfileCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = Profile_serializer
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = Profile_serializer
    lookup_field = 'email'

    def get_queryset(self):
        email = self.kwargs['email']
        return Profile.objects.filter(email = email)
    
class DataHistoryCreate(generics.ListCreateAPIView):
    queryset = DataHistory.objects.all()
    serializer_class = DataHistory_serializer

class DataHistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataHistory.objects.all()
    serializer_class = DataHistory_serializer
    lookup_field = 'email'

    def get_queryset(self):
        email = self.kwargs['email']
        return Profile.objects.filter(email = email)
