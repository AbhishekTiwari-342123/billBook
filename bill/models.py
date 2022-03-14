from django.db import models

# Create your models here.


# Distributor Groups
class Distributor_Group(models.Model):
    Distributor_Group_Id=models.CharField(max_length=10,primary_key=True)
    Distributor_Group_Name=models.CharField(max_length=20, default="")

    def __str__(self):
        return self.Distributor_Group_Name

# Product
class Product(models.Model):
    Product_Id=models.CharField(max_length=10,primary_key=True)
    Product_Name=models.CharField(max_length=20, default="")
    Product_Rate=models.IntegerField(default=0)
    
    def __str__(self):
        return self.Product_Name

# Farmer Group
class Farmer_Group(models.Model):
    Farmer_Group_Id=models.CharField(max_length=10,primary_key=True)
    Farmer_Group_Name=models.CharField(max_length=20, default="")

    def __str__(self):
        return self.Farmer_Group_Name

# Distributor
class Distributor(models.Model):
    Ditributor_Id = models.CharField(max_length=10,primary_key=True)
    Group_Name=models.ForeignKey(Distributor_Group, on_delete=models.CASCADE)
    Name=models.CharField(max_length=20, default="")
    Address=models.CharField(max_length=150, default="")
    Mobile=models.IntegerField(default=0)

    def __str__(self):
        return self.Name

# Customer   
class Customer(models.Model):
    Customer_Id = models.CharField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=20, default="")
    Distributor_Name=models.ForeignKey(Distributor,on_delete=models.CASCADE)
    Address=models.CharField(max_length=150, default="")
    Mobile=models.IntegerField(default=0)

    def __str__(self):
        return self.Name

# Customer Income
class CustomerIncome(models.Model):
    
    class Meta:
        unique_together=(('Customer_Id','Date'))
    
    Customer_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Date=models.DateField(auto_now=False)
    Time=models.CharField(max_length=20, default="Morning")
    Product_Id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.FloatField(default=0)
    Rate=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)
    isPaid=models.BooleanField(default=False)
    

# Farmer
class Farmer(models.Model):
    Farmer_Id = models.CharField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=20, default="")
    Farmer_Group=models.ForeignKey(Farmer_Group,on_delete=models.CASCADE)
    Address=models.CharField(max_length=150, default="")
    Mobile=models.IntegerField(default=0)

# Farmer Expenditure
class FarmerExpenditure(models.Model):
    Farmer_Id = models.ForeignKey(Farmer,on_delete=models.CASCADE)    
    Date=models.DateField(auto_now=False)
    Time=models.CharField(max_length=20, default="Morning")
    Product_Id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=0)
    Rate=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)

# Distributor Expenditure
class DistributorExpenditure(models.Model):
    Distributor_Id=models.ForeignKey(Distributor,on_delete=models.CASCADE)
    Date=models.DateField(auto_now=False)
    Time=models.CharField(max_length=20, default="Morning")
    Product_Id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=0)
    Rate=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)
    
class Carrier(models.Model):
    Carrier_Id=models.CharField(max_length=40,primary_key=True)
    Name=models.CharField(max_length=40, default="")
    Address=models.CharField(max_length=150, default="")
    Mobile=models.IntegerField(default=0)

class CarrierExpenditure(models.Model):
    Carrier_Id=models.ForeignKey(Carrier, on_delete=models.CASCADE)
    Date=models.DateField(auto_now=False)
    Time=models.CharField(max_length=40, default="Morning")
    Product_Id=models.ForeignKey(Product,on_delete=models.CASCADE)
    Quantity=models.IntegerField(default=0)
    Rate=models.IntegerField(default=0)
    Paid=models.IntegerField(default=0)
    Due=models.IntegerField(default=0)
    isPaid=models.BooleanField(default=False)

class Rates(models.Model):
    Quality_Check=models.FloatField(default=1)
    Carrier_Charges=models.FloatField(default=2.5)
    Distributon_Chagres=models.FloatField(default=2.0)
    Marketing_Charges=models.FloatField(default=1.0)
    Other_Charges=models.FloatField(default=1.0)