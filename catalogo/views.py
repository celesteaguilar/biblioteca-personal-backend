from rest_framework import viewsets

from .models import Autor
from .serializers import AutorSerializer


class AutorViewSet(viewsets.ReadOnlyModelViewSet):
    # Sesion 11: solo lectura (listar y ver detalle).
    # El CRUD completo se agrega en la Sesion 13.
    queryset = Autor.objects.all().order_by("id")
    serializer_class = AutorSerializer