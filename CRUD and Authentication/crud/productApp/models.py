from django.db import models

# Create your models here.
class Product(models.Model):
    Procurement_Plaform = models.CharField(max_length=50)
    Product_name = models.CharField(max_length=50)
    Employ_ID = models.CharField(max_length=100)
    THD_Dept = models.CharField(max_length=15)
    Unit_Price = models.CharField(max_length=100)
    Purchasing_Links = models.CharField(max_length=50)
    Product_Category = models.CharField(max_length=50)
    Qty_Available = models.CharField(max_length=10)
    
    def __str__(self):
        return(f"{self.Product_name}")