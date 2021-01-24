from rest_framework import serializers
from .models import profile

class profileSer(serializers.ModelSerializer):
    class Meta:
        model= profile
        fields = ['id', 'name', 'designation', 'empid']

