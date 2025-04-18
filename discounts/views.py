from rest_framework import viewsets
from .models import Discount
from .serializers import DiscountSerializer
from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        """
        Grant permissions based on the action
        """
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated(), IsAdminUser()]  # Only admins can create, update, or delete discounts
        elif self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]  # Both admins and authenticated users can list and view discounts
        return [IsAuthenticated()]
