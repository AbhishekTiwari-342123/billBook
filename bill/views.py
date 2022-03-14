from django.shortcuts import render,redirect
from tablib import Dataset
from .resources import CustomerResource, DistributorResource, FarmerResource
from .models import *
from django.db.models.aggregates import Sum


# final
# commited
def home(request):
    return render(request,'bill/home.html')

# final
# commited
def add_distributor_group(request):
    if request.method=='POST':
        print(request.POST)
        
        #creating objects of the model for insertion of new record
        DG_OBJ=Distributor_Group()
         
        #adding distributor group details
        DG_OBJ.Distributor_Group_Id=request.POST.get('d_g_id')
        DG_OBJ.Distributor_Group_Name=request.POST.get('d_g_name')
       
        DG_OBJ.save()
    
        return redirect('add-dg')
    return render(request,'bill/d_group_form.html')    

# final
# commited
def add_farmer_group(request):
    if request.method=='POST':
        print(request.POST)
        
        #creating objects of the model for insertion of new record
        FG_OBJ=Farmer_Group()
         
        #adding distributor group details
        FG_OBJ.Farmer_Group_Id=request.POST.get('f_g_id')
        FG_OBJ.Farmer_Group_Name=request.POST.get('f_g_name')
       
        FG_OBJ.save()
    
        return redirect('add-fg')
    return render(request,'bill/f_group_form.html')

def add_farmer(request):
    if request.method=='POST':
        print(request.POST)
        
        #creating objects of the model for insertion of new record
        Farmer_OBJ=Farmer(Farmer_Id=request.POST.get('far_id'),Name=request.POST.get('far_name'), 
        Farmer_Group = Farmer_Group.objects.get(Farmer_Group_Name=request.POST.get('far_grp')),
        Address=request.POST.get('far_add'),Mobile=request.POST.get('far_mob'))
       
        Farmer_OBJ.save()
    
        return redirect('add-f')
    else:
        farmerGroups=Farmer_Group.objects.all()
        return render(request,'bill/add_farmer.html',{'farmerGroups':farmerGroups})   

# final
# commited
def add_product(request):
    if request.method=='POST':
        print(request.POST)
        
        #creating objects of the model for insertion of new record
        P_OBJ=Product()
         
        #adding distributor group details
        P_OBJ.Product_Id=request.POST.get('p_id')
        P_OBJ.Product_Name=request.POST.get('p_name')
        P_OBJ.Product_Rate=request.POST.get('p_rate')
        
       
        P_OBJ.save()
    
        return redirect('add-p')
    return render(request,'bill/product_form.html')    

# final
# commited
def add_distributor(request):
    if request.method=='POST':
        print(request.POST)
        
        #creating objects of the model for insertion of new record
        D_OBJ=Distributor(Ditributor_Id = Distributor_Group.objects.get(Distributor_Group_Name=request.POST.get('d_id')),
        Name=request.POST.get('d_name'),Address=request.POST.get('d_address'),Mobile=request.POST.get('d_mobile'))
       
        D_OBJ.save()
    
        return redirect('add-d')
    else:
        context=Distributor_Group.objects.all()
        distributors=Distributor.objects.all()
        return render(request,'bill/distributor_form.html',{'context':context, 'distributors':distributors})
# final
# commited
def add_customer(request):
    if request.method=="POST":
        print(request)
        New_Customer=Customer()
        New_Customer.Customer_Id=request.POST.get('cus_id')
        New_Customer.Name=request.POST.get('cus_name')
        New_Customer.Distributor_Name=Distributor.objects.get(Name=request.POST.get('cus_dis'))
        New_Customer.Address=request.POST.get('cus_add')
        New_Customer.Mobile=request.POST.get('cus_mob')
        New_Customer.save()
        return redirect('add-c')
        
    else:
        distributors_name= Distributor.objects.all()
        customers= Customer.objects.all()
        print(distributors_name)
        return render(request,'bill/add_customer.html',{'distributors':distributors_name,'customers':customers})

def add_carrier(request):
    if request.method=="POST":
        print(request)
        New_Carrier=Carrier()
        New_Carrier.Carrier_Id=request.POST.get('car_id')
        New_Carrier.Name=request.POST.get('car_name')
        New_Carrier.Address=request.POST.get('car_add')
        New_Carrier.Mobile=request.POST.get('car_mob')
        New_Carrier.save()
        return redirect('add-car')
        
    else:
        carriers= Carrier.objects.all()
        return render(request,'bill/add_carrier.html',{'carriers':carriers})


# final
# commited
def customer_transaction_daily(request):
    if request.method=="POST":
        print('1 ',request.POST)
        if "importData" in request.POST:
            print('2 ','reached import scope')
            customer_income_resource = CustomerResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            print('3 ',imported_data)
            result = customer_income_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                customer_income_resource.import_data(dataset, dry_run=False)  # Actually import now
        else:    
            print('4 ',request.POST)
            NewCustomerIncome= CustomerIncome(
            Customer_Id=Customer.objects.get(Customer_Id=request.POST.get('id')),Date=request.POST.get('date'),
            Time=request.POST.get('time'),Product_Id=Product.objects.get(Product_Id=request.POST.get('product')),
            Quantity=request.POST.get('quantity'),Rate=request.POST.get('rate'),
            Paid=request.POST.get('paid'),Due=request.POST.get('due'))
            NewCustomerIncome.save()

        return redirect('add-ctd')
    else:
        products=Product.objects.all()
        customers=Customer.objects.all()
        return render(request,'bill/customer_daily_transaction.html',
        {'products':products,'customers':customers})

# final
# comited
def distributor_transaction_daily(request):
    if request.method=="POST":
        print('1 ',request.POST)
        if "importData" in request.POST:
            print('2 ','reached import scope')
            distributor_expenditure_resource = DistributorResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            print('3 ',imported_data)
            result = distributor_expenditure_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                distributor_expenditure_resource.import_data(dataset, dry_run=False)  # Actually import now
        else:    
            print('4 ',request.POST)
            NewDistributorExpenditure= DistributorExpenditure(
            Customer_Id=Distributor.objects.get(Distributor_Id=request.POST.get('id')),Date=request.POST.get('date'),
            Time=request.POST.get('time'),Product_Id=Product.objects.get(Product_Id=request.POST.get('product')),
            Quantity=request.POST.get('quantity'),Rate=request.POST.get('rate'),
            Paid=request.POST.get('paid'),Due=request.POST.get('due'))
            NewDistributorExpenditure.save()

        return redirect('add-dtd')
    else:
        products=Product.objects.all()
        distributors=Distributor.objects.all()
        return render(request,'bill/distributor_daily_transactions.html',
        {'products':products,'distributors':distributors})

# final
# comited
def farmer_transaction_daily(request):
    if request.method=="POST":
        print('1 ',request.POST)
        if "importData" in request.POST:
            print('2 ','reached import scope')
            farmer_expenditure_resource = FarmerResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']

            imported_data = dataset.load(new_persons.read())
            print('3 ',imported_data)
            result = farmer_expenditure_resource.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                farmer_expenditure_resource.import_data(dataset, dry_run=False)  # Actually import now
        else:    
            print('4 ',request.POST)
            NewFarmerExpenditure= FarmerExpenditure(
            Farmer_Id=Farmer.objects.get(Farmer_Id=request.POST.get('id')),Date=request.POST.get('date'),
            Time=request.POST.get('time'),Product_Id=Product.objects.get(Product_Id=request.POST.get('product')),
            Quantity=request.POST.get('quantity'),Rate=request.POST.get('rate'),
            Paid=request.POST.get('paid'),Due=request.POST.get('due'))
            NewFarmerExpenditure.save()

        return redirect('add-dtd')
    else:
        products=Product.objects.all()
        farmers=Farmer.objects.all()
        return render(request,'bill/farmer_daily_transactions.html',
        {'products':products,'farmers':farmers})

# main aggregate page 
def consumer_aggregate(request):
    Customers = Customer.objects.all() 
    Distributors=Distributor.objects.all()
    return render(request,"bill/consumer_aggregate.html",{'Customers':Customers,'Distributors':Distributors})

# aggregate consumer of main aggregate page
def consumer_aggregate_one(request):
    print(request.GET)
    fdate=request.GET.get('fdate')
    tdate=request.GET.get('tdate')
    print(fdate,tdate)
    Consumer_Records=CustomerIncome.objects.filter(Date__range=[fdate,tdate],
    Customer_Id=request.GET.get('CustomerId'))
    Consumer_Transactions=CustomerIncome.objects.filter(Date__range=[fdate,tdate],
    Customer_Id=request.GET.get('CustomerId')).aggregate(Total_Paid=Sum('Paid'), Total_Due=Sum('Due'))
    print(Consumer_Transactions)
    return render(request,"bill/AggrTab.html",{'data':Consumer_Transactions, 'records':Consumer_Records})

# aggregate distributor of main aggregate page
def distributor_aggregate_one(request):
    print(request.GET)
    fdate=request.GET.get('fdate')
    tdate=request.GET.get('tdate')
    print(fdate,tdate)
    Distributor_Records=DistributorExpenditure.objects.filter(Date__range=[fdate,tdate],
    Distributor_Id=request.GET.get('DistributorId'))
    print(Distributor_Records)
    Distributor_Transactions=DistributorExpenditure.objects.filter(Date__range=[fdate,tdate],
    Distributor_Id=request.GET.get('DistributorId')).aggregate(Total_Paid=Sum('Paid'), Total_Due=Sum('Due'))
    print(Distributor_Transactions)
    return render(request,"bill/AggrTab.html",{'data':Distributor_Transactions, 'records':Distributor_Records}) 

# 
def balance(request):
    Customers = Customer.objects.all()
    return render(request,"bill/balance.html",{'Customers':Customers})         

# deducts the customer due balance by the amount paid 
def balanceCustomer(request):
    Customer_Id=request.GET.get('CustomerId')
    CustomerDue=CustomerIncome.objects.filter(Customer_Id=Customer_Id)
    paid_amount=int(request.GET.get('pay'))
    i=0 
    counter=CustomerDue.count()
    print(CustomerDue.count())
    # deduct until the paid amount becomes zero
    while(paid_amount > 0 and i < counter):
        # deduct and delete if due is smaller or equal to paid amount
        print(i,paid_amount)
        print(CustomerDue[i].Date,CustomerDue[i].Customer_Id,CustomerDue[i].Due)
        if CustomerDue[i].Due <= paid_amount and CustomerDue[i].isPaid==False:
            print("2 ",CustomerDue[i].Due)
            paid_amount=paid_amount-CustomerDue[i].Due
            print("2 ",paid_amount)
            CustomerIncome.objects.filter(Customer_Id=Customer_Id,Date=CustomerDue[i].Date).update(Due=0, isPaid=True)
        # dedcut and update if due is bigger than paid amount, set the due by the diminishing the paid amount
        elif CustomerDue[i].Due >= paid_amount:
            print("3 ",CustomerDue[i].Due)
            new_due=CustomerDue[i].Due-paid_amount
            print("3 ",new_due)
            # setting the paid amount to negative after new due to break the while loop
            paid_amount=paid_amount-CustomerDue[i].Due
            CustomerIncome.objects.filter(Customer_Id=Customer_Id,Date=CustomerDue[i].Date).update(Due=new_due)
        i=i+1
    DueRemaining=CustomerIncome.objects.filter(Customer_Id=Customer_Id,isPaid=False)
    Consumer_Transactions=CustomerIncome.objects.filter(Customer_Id=Customer_Id)\
        .aggregate(Total_Paid=Sum('Paid'), Total_Due=Sum('Due'))
    return render(request,"bill/BalTab.html",{'DueRemaining':DueRemaining, 'data':Consumer_Transactions})       

def update(request,id):
    try:
        Customer_edit=Customer.objects.get(Customer_Id=id)
        Customer_edit.Name=request.GET.get('Name')
        print(Customer_edit.Name)
        Customer_edit.Distributor_Name=Distributor.objects.get(Name=request.GET.get('Distributor_Name'))
        Customer_edit.Address=request.GET.get('Address')
        Customer_edit.Mobile=request.GET.get('Mobile')
        Customer_edit.save()
        print(request.GET)
        print(id)
        return redirect('add-c') 
    except:
        return redirect('add-c')

# delete customer
def delete(request,id):
    Customer_delete=Customer.objects.get(Customer_Id=id).delete()
    return redirect('add-c')

# delete distributor 
def delete_d(request,id):
    Distributor_delete=Distributor.objects.get(Ditributor_Id=id).delete()
    return redirect('add-d')

# update distributor
def update_d(request,id):
    try:
        Distributor_edit=Distributor.objects.get(Ditributor_Id=id)
        Distributor_edit.Name=request.GET.get('Name')
        print(Distributor_edit.Name)
        Distributor_edit.Group_Name=Distributor_Group.objects.get(Distributor_Group_Name=request.GET.get('Distributor_Group_Name'))
        Distributor_edit.Address=request.GET.get('Address')
        Distributor_edit.Mobile=request.GET.get('Mobile')
        Distributor_edit.save()
        print(request.GET)
        print(id)
        return redirect('add-d')
    except:
        return redirect('add-d')

def update_car(request,id):
    try:
        Carrier_edit=Carrier.objects.get(Carrier_Id=id)
        Carrier_edit.Name=request.GET.get('Name')
        print(Carrier_edit.Name)
        Carrier_edit.Address=request.GET.get('Address')
        Carrier_edit.Mobile=request.GET.get('Mobile')
        Carrier_edit.save()
        print(request.GET)
        print(id)
        return redirect('add-car')
    except:
        return redirect('add-car')        