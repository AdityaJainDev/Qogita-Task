from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['sku', 'barcode', 'id']
    search_fields = ['title', 'sku', 'barcode']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    http_method_names = ['get', 'post']
