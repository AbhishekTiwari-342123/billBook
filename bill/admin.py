from bill.resources import *
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CustomerAdmin(ImportExportModelAdmin):
    list_display=['Customer_Id','Name','Distributor_Name','Address','Mobile']
    resource_class=CustomerResource

class CustomerIncomeAdmin(ImportExportModelAdmin):
    list_display=['Customer_Id','Date','Time','Product_Id','Quantity','Rate','Paid','Due','isPaid']
    resource_class=CustomerIncomeResource

class DistributorExpenditureAdmin(ImportExportModelAdmin):
    list_display=['Distributor_Id','Date','Time','Product_Id','Quantity','Rate','Paid','Due']
    resource_class=DistributorResource

class FarmerExpenditureAdmin(ImportExportModelAdmin):
    list_display=['Farmer_Id','Date','Time','Product_Id','Quantity','Rate','Paid','Due']
    resource_class=FarmerResource

class CarrierExpenditureAdmin(ImportExportModelAdmin):
    list_display=['Carrier_Id','Date','Time','Product_Id','Quantity','Rate','Paid','Due','isPaid']
    resource_class=CarrierExpenditureResource

admin.site.register(Distributor_Group)
admin.site.register(Product)
admin.site.register(Farmer_Group)
admin.site.register(Distributor)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Farmer)
admin.site.register(Carrier)
admin.site.register(Rates)
admin.site.register(CustomerIncome,CustomerIncomeAdmin)
admin.site.register(FarmerExpenditure,FarmerExpenditureAdmin)
admin.site.register(DistributorExpenditure,DistributorExpenditureAdmin)
admin.site.register(CarrierExpenditure,CarrierExpenditureAdmin)



