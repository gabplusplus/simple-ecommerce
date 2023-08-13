from rest_framework import generics, permissions
from .models import Checkout
from .serializers import CheckoutSerializer


class CheckoutCreate(generics.CreateAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Checkout.objects.all()


class CheckoutList(generics.ListAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Checkout.objects.all()


class CheckoutDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Checkout.objects.all()
    lookup_field = 'pk'