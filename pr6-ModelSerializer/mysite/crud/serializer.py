from rest_framework import serializers
from .models import student


#IN model serializer we dont need to write code for create and update
class studentSerializer(serializers.ModelSerializer):

    #validators
    def reg_equal_to_1(value):
        if value !=1:
            raise serializers.ValidationError('Reg must be 1')
        return value

    reg_no = serializers.IntegerField(validators=[reg_equal_to_1])
    class Meta:
        model = student
        fields = '__all__'

    #field level validation
    def validate_reg_no(self,value):
        if value!=1:
            raise serializers.ValidationError('REG NO MUST BE 1')
        return value

    #object level validation
    def validate(self,data):
        name = data.get('name')
        reg_no = data.get('reg_no')

        if name.lower() !='nimra' or reg_no != 1:
            raise serializers.ValidationError('name must be nimra or reg must be equal to 1')
        return data






   

