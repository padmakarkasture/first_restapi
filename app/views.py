from django.shortcuts import render
from rest_framework import viewsets
from .models import profile
from app.serializers import profileSer
from rest_framework import renderers
  
# Create your views here.
class profile_viewset(viewsets.ModelViewSet):
    queryset=profile.objects.all()
    serializer_class=profileSer
    renderer_classes = [renderers.JSONRenderer]

