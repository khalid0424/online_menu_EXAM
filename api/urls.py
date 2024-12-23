from django.urls import path , include
from rest_framework.routers import DefaultRouter

from .views import CategoriesViewSet ,ModelViewSet, BillViewSet,OrdersViewSet , RestrauntTableViewSet

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'models', ModelViewSet, basename='models')
router.register(r'bills', BillViewSet, basename='bills')
router.register(r'orders', OrdersViewSet, basename='orders')
router.register(r'restraunt-tables', RestrauntTableViewSet, basename='restraunt-tables')




urlpatterns = [
    path('api/', include(router.urls))
]
  