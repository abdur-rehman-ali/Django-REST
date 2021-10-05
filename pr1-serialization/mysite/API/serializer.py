from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    #explicitly mention id attribute if you want to include id in your response
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    reg_no = serializers.IntegerField()
    faculty = serializers.CharField(max_length=20)