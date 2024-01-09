from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователя"""
    new_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'new_password', 'name']

    def save(self, *args, **kwargs):
        """Метод для сохранения нового пользователя"""
        # Проверяем на валидность пароли
        password = self.validated_data['password']
        new_password = self.validated_data['new_password']
        # Если пароли не валидны, то возбуждаем ошибку
        if password != new_password:
            raise serializers.ValidationError("Password doesn't match")
        # Cоздаем пользователя
        user = User.objects.create(
            email=self.validated_data.get('email'),
            name=self.validated_data.get('name', None),
        )
        # Сохраняем пароль
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя (просмотр, изменение, удаление)"""
    class Meta:
        model = User
        fields = ('email', 'name')