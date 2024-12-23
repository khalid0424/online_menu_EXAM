from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Categories,Meal,Orders,RestrauntTable,Bill
from .serializers import * 


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all
    serializer_class = MealSerializer

class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all
    serializer_class = OrdersSerializer

class RestrauntTableViewSet(ModelViewSet):
    queryset = RestrauntTable.objects.all
    serializer_class = RestrauntTableSerializer
class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all
    serializer_class = BillSerializer

class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


















