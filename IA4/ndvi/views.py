from .models import NDVIModel
from .serializers import NDVISerializer
from rest_framework import viewsets
from .calculation import ndvi_values

class NDVIView(viewsets.ModelViewSet):
    queryset = NDVIModel.objects.all()
    serializer_class = NDVISerializer