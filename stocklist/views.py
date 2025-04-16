from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['sku', 'barcode', 'id']
    search_fields = ['title', 'sku', 'barcode']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    http_method_names = ['get', 'delete']
    pagination_class = ProductPagination
