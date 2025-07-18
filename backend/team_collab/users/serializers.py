from .models import User
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
                phone=validated_data['phone'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user