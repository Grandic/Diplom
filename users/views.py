from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsUser
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Create new user"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    class Meta:
        model = User
        fields = '__all__'



class UserListAPIView(generics.ListAPIView):
    """ Users List """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    class Meta:

        model = User
        fields = '__all__'


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ User detail """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateAPIView(generics.UpdateAPIView):
    """ User update"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsUser]

    class Meta:
        model = User
        fields = '__all__'



class UserDestroyAPIView(generics.DestroyAPIView):
    """ User delete """

    queryset = User.objects.all()
    permission_classes = [IsUser]

    class Meta:
        model = User
        fields = '__all__'

