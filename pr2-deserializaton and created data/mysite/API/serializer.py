from rest_framework import serializers
from .models import student

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    reg_no = serializers.IntegerField()
    faculty = serializers.CharField(max_length=50)

    
    def create(self,validated_data):
        """
        This function is responsible for saving data in student model of database
        """
        return student.objects.create(**validated_data)