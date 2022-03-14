from import_export import resources
from .models import *

class CustomerIncomeResource(resources.ModelResource):
    class Meta:
        model = CustomerIncome
        # import_id_fields=['',]

class DistributorResource(resources.ModelResource):
    class Meta:
        model = DistributorExpenditure
        import_id_fields=['',]

class FarmerResource(resources.ModelResource):
    class Meta:
        model = FarmerExpenditure
        import_id_fields=['',]

class CustomerResource(resources.ModelResource):
    class Meta:
        model=Customer
        import_id_fields=['Customer_Id',]

class CarrierExpenditureResource(resources.ModelResource):
    class Meta:
        model = CarrierExpenditure
        import_id_fields=['',]        