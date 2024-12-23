from rest_framework import serializers
from .models import  Categories, Meal , Orders,Bill,RestrauntTable  


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        
class RestrauntTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestrauntTable
        fields = '__all__'





