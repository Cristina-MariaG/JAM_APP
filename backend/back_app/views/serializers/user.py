# users/serializers.py

from rest_framework import serializers

from back_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User

        fields = ("id", "email", "password")
