from django.urls import path
from .views import (
    CustomerRegisterView, DeliveryAgentListCreateView,
    DeliveryAgentDetailView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='customer-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delivery-agents/', DeliveryAgentListCreateView.as_view(), name='delivery-agent-list'),
    path('delivery-agents/<int:pk>/', DeliveryAgentDetailView.as_view(), name='delivery-agent-detail'),
]
