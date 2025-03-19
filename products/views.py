from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminRole


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can view

    def get_permissions(self):
        if self.request.method == 'POST':  # Only restrict creation
            return [IsAdminRole()]
        return [IsAuthenticated()]  # Only logged-in users can view


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminRole]  # Only admin users can edit/delete
