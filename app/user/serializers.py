"""
Serializers for the user API view.
"""
from pyexpat import model
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwarg = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
