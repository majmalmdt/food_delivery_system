from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User
from .serializers import DeliveryAgentSerializer, UserSerializer, CustomerRegisterSerializer
from .permissions import IsAdmin, IsDeliveryAgent

# 🔹 Customer Registration
class CustomerRegisterView(generics.CreateAPIView):
    queryset = User.objects.filter(role='customer')
    serializer_class = CustomerRegisterSerializer
    permission_classes = [permissions.AllowAny]

# 🔹 Admin: Manage Delivery Agents
class DeliveryAgentListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='delivery_agent', is_deleted=False)
    serializer_class = DeliveryAgentSerializer
    permission_classes = [IsAdmin]

class DeliveryAgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='delivery_agent', is_deleted=False)
    serializer_class = DeliveryAgentSerializer
    permission_classes = [IsAdmin]

    def destroy(self, request, *args, **kwargs):
        agent = self.get_object()
        agent.is_deleted = True  # Soft delete
        agent.save()
        return Response({"message": "Delivery agent soft deleted successfully."})
