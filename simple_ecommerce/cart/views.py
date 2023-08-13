from rest_framework import generics, permissions
from .models import Cart
from .serializers import CartSerializer


class CartCreate(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny,]
    
    def get_queryset(self):
        queryset = Cart.objects.all()
        queryset.filter(checked_out=False)
        return queryset


class CartList(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny,]

    def get_queryset(self):
        queryset = Cart.objects.all()
        queryset.filter(checked_out=False)
        return queryset


class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny,]
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Cart.objects.all()
        queryset.filter(checked_out=False)
        return queryset