from rest_framework.routers import DefaultRouter
from .views import DiscountViewSet

router = DefaultRouter()
router.register('', DiscountViewSet, basename='discounts')

urlpatterns = router.urls
