from rest_framework import serializers
from .models import MPackage

class MPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MPackage
        fields = ['package_name','package_desc']