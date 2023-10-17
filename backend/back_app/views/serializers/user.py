from rest_framework import serializers

from back_app.models import User
from back_app.views.serializers.role import RoleSerializer


# class UserSerializer(serializers.ModelSerializer):
#     role = RoleSerializer()

#     class Meta(object):
#         model = User

#         fields = ("id", "email", "password", "role")
# class UserSerializer(serializers.ModelSerializer):
#     role = RoleSerializer()
#     class Meta:
#         model = User
#         fields = ["id", "email",  "role"]


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
