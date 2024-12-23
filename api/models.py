from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    is_active = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_datetime = models.DateTimeField(auto_now_add=True)

    image_file = models.ImageField(upload_to='meals/')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class RestrauntTable(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('full', 'Full'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='free')
    table_num = models.IntegerField()

    def __str__(self):
        return self.table_num

class Bill(models.Model):
    table = models.ForeignKey(RestrauntTable, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    total_sum = models.DecimalField(max_digits=5, decimal_places=2)
    created_datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Bill for {self.customer} at table {self.table.table_num}"
    
class Orders(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.quantity} x {self.meal.name} for bill {self.bill.id}"





    





