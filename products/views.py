from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer, ProductPriceSerializer
from .permissions import IsAdminUser  # Custom permission to check for admin user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admins can manage products
    authentication_classes = [JWTAuthentication]



class ProductPriceViewSet(viewsets.ViewSet):
    """
    View for getting product price based on type and quantity.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def retrieve(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        quantity = request.query_params.get('quantity', 1)  # Default to 1 if not provided
        quantity = int(quantity)

        # Calculate price based on the product type
        calculated_price = product.get_price(quantity)

        response_data = {
            "id": product.id,
            "name": product.name,
            "base_price": str(product.base_price),  # Convert to string for safe JSON serialization
            "type": product.get_type_display(),  # Get human-readable product type
            "calculated_price": str(calculated_price),  # Convert price to string for safety
        }

        # Return the response with product details and calculated price
        return Response(response_data)
