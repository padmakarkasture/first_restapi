from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import profile
from app.serializers import profileSer
from rest_framework import renderers
from rest_framework import authentication
from rest_framework import permissions
  
# Create your views here.
class profile_viewset(viewsets.ModelViewSet):
    queryset=profile.objects.all()
    serializer_class=profileSer
    renderer_classes = [renderers.JSONRenderer]
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.DjangoModelPermissions]
