from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from user_profile.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm=serializers.CharField(max_length=255,write_only=True)

    class Meta:
        model=User
        fields=['user_name','email','password','password_confirm']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"details":"passwords does not match"})
        
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as errors:
            raise serializers.ValidationError({'password':list(errors.messages)})
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password_confirm',None)
        return User.objects.create_user(**validated_data)
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "user_name"
    
    def validate(self, attrs):
        validated_data=super().validate(attrs)
        validated_data['user_name']=self.user.user_name
        validated_data['email']=self.user.email
        if not self.user.is_verified:
            raise serializers.ValidationError({"detail":"user is not verified"})
        return validated_data