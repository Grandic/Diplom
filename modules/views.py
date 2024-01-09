from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from modules.models import Module
from modules.paginators import ModulesPaginator
from modules.permissions import IsOwner
from modules.serializers import ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    "Контролер для создания модуля"
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_modul = serializer.save()
        new_modul.owner = self.request.user
        new_modul.save()


class ModuleListAPIView(generics.ListAPIView):
    "Контролер для просмотра списка модулей"
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulesPaginator


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра одного модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления модуля"""
    serializer_class = ModuleSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Module.objects.filter(owner=self.request.user)


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления модуля"""
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsOwner]