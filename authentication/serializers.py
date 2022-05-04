from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Student

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
        }


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ("photo_embeddings",)
