from rest_framework import generics, permissions
from .models import Products
from .serializers import ProductSerializer


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Products.objects.all()


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Products.objects.all()


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Products.objects.all()
    lookup_field = 'pk'