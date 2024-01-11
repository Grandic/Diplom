from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['first_name', 'date_joined', 'last_login', 'groups', 'user_permissions',
                   'is_superuser', 'is_staff', 'is_active', 'last_name', 'password']
