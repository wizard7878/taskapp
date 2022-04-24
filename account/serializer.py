from rest_framework import serializers
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        max_length=150, 
        write_only=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model  =  User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style' : {'input_type': 'password'}
            },
        }

    def validate(self, data):
        """
        Check that password is equal with confirm_password
        """

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password must be equal with confirm_password')
        return data
        