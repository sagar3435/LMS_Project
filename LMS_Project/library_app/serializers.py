from rest_framework import serializers
from .models import Admin, Book
from django.contrib.auth import authenticate

class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Admin
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        return Admin.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        admin = authenticate(**data)
        if not admin:
            raise serializers.ValidationError("Invalid credentials")
        return {'admin': admin}

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
