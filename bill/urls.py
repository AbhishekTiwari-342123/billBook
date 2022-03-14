from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home  ,name="home"),
    
    # Add Data 
    path('add-distributor-group/', views.add_distributor_group  ,name="add-dg"),
    path('add-farmer-group/', views.add_farmer_group  ,name="add-fg"),
    path('add-product/', views.add_product  ,name="add-p"),
    path('add-distributor/', views.add_distributor  ,name="add-d"),
    path('add-customer/', views.add_customer  ,name="add-c"),
    path('add-farmer/', views.add_farmer  ,name="add-f"),
    path('add-carrier/', views.add_carrier  ,name="add-car"),
    path('add-customerTransaction/', views.customer_transaction_daily  ,name="add-ctd"),
    path('add-distributorTransaction/', views.distributor_transaction_daily  ,name="add-dtd"),
    path('add-farmerTransaction/', views.farmer_transaction_daily  ,name="add-ftd"),
    
    # Aggregate
    path('get-consumerAggregate/', views.consumer_aggregate  ,name="add-ca"),
    path('get-consumerAggregateO/', views.consumer_aggregate_one  ,name="add-cao"),
    path('get-distributorAggregateO/', views.distributor_aggregate_one  ,name="add-dao"),
    
    # Balance
    path('get-Balance/', views.balance  ,name="add-bal"),
    path('get-CustomerBalance/', views.balanceCustomer  ,name="add-cbal"),
    
    # Update
    path('add-customer/list/update/<id>', views.update, name="update"),
    path('add-distributor/list/update/<id>', views.update_d, name="update_d"),
    path('add-carrier/list/update/<id>', views.update_car, name="update_car"),
    
    # delete
    path('add-customer/delete/<id>', views.delete, name="delete"),
    path('add-distributor/delete/<id>', views.delete_d, name="delete_d")
    
    
    
]