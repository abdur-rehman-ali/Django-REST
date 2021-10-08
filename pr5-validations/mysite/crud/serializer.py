from rest_framework import serializers
from .models import student

#validators
def reg_equal_to_1(value):
    if value !=1:
        raise serializers.ValidationError('Reg must be 1')
    return value


class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    reg_no = serializers.IntegerField(validators=[reg_equal_to_1])

    #field level validation
    def validate_reg_no(self,value):
        if value>50000:
            raise serializers.ValidationError('REG NO MUST BE LESS THAN 50000')
        return value

    #object level validation
    def validate(self,data):
        name = data.get('name')
        reg_no = data.get('reg_no')

        if name.lower() !='nimra' and reg_no != 30000:
            
            raise serializers.ValidationError('name must be nimra and  reg must be equal to 3000')
        return data

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