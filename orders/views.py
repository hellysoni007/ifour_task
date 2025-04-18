from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get_queryset(self):
        """
        Filter orders based on the logged-in user.
        """
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be authenticated to view orders.")
        
        if user.is_admin:
            return Order.objects.all()  # Admins can see all orders
        return Order.objects.filter(user=user)  # Users can only see their own orders

    def perform_create(self, serializer):
        """
        Assign the current user to the order.
        """
        serializer.save(user=self.request.user)  # Set the current user as the owner of the order

