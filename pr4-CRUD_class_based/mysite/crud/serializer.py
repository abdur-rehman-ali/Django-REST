from rest_framework import serializers
from .models import student

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    reg_no = serializers.IntegerField()

    def create(self,validated_data):
        """
        This function is responsible for saving data in student model of database
        """
        return student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        This function is responsible for updating data in student model of database
        instance = previous data
        validated_data = new data
        """
        instance.name = validated_data.get('name', instance.name)
        instance.reg_no = validated_data.get('reg_no', instance.reg_no)
        instance.save()
        return instance