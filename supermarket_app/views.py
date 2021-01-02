from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from supermarket_app.forms import VendorForm,ManagerForm,ItemsForm,StocksForm,SupplyForm,ProductInstanceForm,DiscardForm,CategoryForm
from supermarket_app.models import Vendor,Manager,Items,Stocks,Supply,Product_Instance,Discarded_Products,Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        

        if password==password:
            if User.objects.filter(username=username).exists():
               messages.info(request,'username Taken')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'email Taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'User Created')
                return render(request,'admin_page.html')
        else:
            print('Password not matching')
        return render(request,'admin_page.html')
        
    else:   
        return render(request,'registrationform.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        return render(request,'supermarket_frontpage.html')
        if user is not None:
            auth.login(request,user)
            return render(request,'supermarket_frontpage.html')
        else:
            messages.info(request,'Invalid Credentials')
            
    else:
        return render(request,'loginform.html')




def supmk(request):
	if request.method == 'POST':
		if request.POST.get('vendor_id') and request.POST.get('location') and request.POST.get('company_name') and request.POST.get('phone_no') and request.POST.get('email'):
			saveRecord = Vendor()
			saveRecord.vendor_id = request.POST.get('vendor_id')
			saveRecord.location = request.POST.get('location')
			saveRecord.company_name = request.POST.get('company_name')
			saveRecord.phone_no = request.POST.get('phone_no')
			saveRecord.email = request.POST.get('email')			
			saveRecord.save()
			messages.success(request, 'Vendor is added successfully!')
			return render(request, 'supermarket_frontpage.html')
	else: 
		return render(request, 'index.html')



def viewVendor(request):
	vendor_table=Vendor.objects.all()
	return render(request,"view_vendor.html",{'vendor_table':vendor_table})

def deleteVendor(request,id):
	vendor_table=Vendor.objects.get(vendor_id=id)
	vendor_table.delete()
	return viewVendor(request)

def editVendor(request,id):
	if request.method == 'POST':
		if request.POST.get('vendor_id') and request.POST.get('location') and request.POST.get('company_name') and request.POST.get('phone_no') and request.POST.get('email'):
			saveRecord = Vendor()
			saveRecord.vendor_id = request.POST.get('vendor_id')
			saveRecord.location = request.POST.get('location')
			saveRecord.company_name = request.POST.get('company_name')
			saveRecord.phone_no = request.POST.get('phone_no')
			saveRecord.email = request.POST.get('email')			
			saveRecord.save()
			messages.success(request, 'Edited successfully!')	
			return viewVendor(request)
	else:
	 	display_table=Vendor.objects.get(vendor_id=id)
	 	return render(request,"edit_vendor.html",{'display_table':display_table})



def mainScreen(request):
	return render(request, 'supermarket_frontpage.html')

def Loginpage(request):
	return render(request,'admin_page.html')

def managerSupmk(request):
	if request.method == 'POST':
		if request.POST.get('mgr_id') and request.POST.get('mgr_name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('sec_name'):
			saveRecord = Manager()
			saveRecord.mgr_id = request.POST.get('mgr_id')
			saveRecord.mgr_name = request.POST.get('mgr_name')
			saveRecord.phone = request.POST.get('phone')
			saveRecord.email = request.POST.get('email')
			saveRecord.sec_name	= request.POST.get('sec_name')	
			saveRecord.save()
			messages.success(request, 'Manager is added successfully!')
			return render(request, 'supermarket_frontpage.html')
	else: 
		return render(request, 'index_manager.html')



def itemsSupmk(request):
	if request.method == 'POST':
		if request.POST.get('item_id') and request.POST.get('price') and request.POST.get('item_name') and request.POST.get('brand'):
			saveRecord = Items()
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.price = request.POST.get('price')
			saveRecord.item_name = request.POST.get('item_name')
			saveRecord.brand = request.POST.get('brand')			
			saveRecord.save()
			messages.success(request, 'Your item is added successfully!')
			return viewItems(request)
	else: 
		return render(request,'index_items.html')

def stocksSupmk(request):
	if request.method == 'POST':
		if request.POST.get('item_id') and request.POST.get('stock_id') and request.POST.get('sec_name') and request.POST.get('quantity') and request.POST.get('unit_price') and request.POST.get('total_price'):
			saveRecord = Stocks()
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.stock_id = request.POST.get('stock_id')
			saveRecord.sec_name = request.POST.get('sec_name')
			saveRecord.quantity = request.POST.get('quantity')
			saveRecord.unit_price = request.POST.get('unit_price')
			saveRecord.total_price = request.POST.get('total_price')			
			saveRecord.save()
			messages.success(request, 'item is added into the stock successfully!')			
			return render(request, 'supermarket_frontpage.html')
	else: 
		return render(request,'index_stocks.html')



def viewItems(request):
	items_table=Items.objects.all()
	return render(request,"view_items.html",{'items_table':items_table})


def viewStocks(request):
	stocks_table=Stocks.objects.all()
	return render(request,"view_stock.html",{'stocks_table':stocks_table})


def editItem(request,id):
	if request.method == 'POST':
		if request.POST.get('item_id') and request.POST.get('price') and request.POST.get('item_name') and request.POST.get('brand'):
			saveRecord = Items()
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.price = request.POST.get('price')
			saveRecord.item_name = request.POST.get('item_name')
			saveRecord.brand = request.POST.get('brand')			
			saveRecord.save()
			messages.success(request, 'Edited successfully!')	
			return viewItems(request)
	else:
	 	display_table=Items.objects.get(item_id=id)
	 	return render(request,"edit_item.html",{'display_table':display_table})
	

def deleteItem(request,id):
	items_table=Items.objects.get(item_id=id)
	items_table.delete()
	return viewItems(request)


def viewManager(request):
	manager_table=Manager.objects.all()
	return render(request,"view_manager.html",{'manager_table':manager_table})

def deleteManager(request,id):
	manager_table=Manager.objects.get(mgr_id=id)
	manager_table.delete()
	return viewManager(request)

def editManager(request,id):
	if request.method == 'POST':
		if request.POST.get('mgr_id') and request.POST.get('mgr_name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('sec_name'):
			saveRecord = Manager()
			saveRecord.mgr_id = request.POST.get('mgr_id')
			saveRecord.mgr_name = request.POST.get('mgr_name')
			saveRecord.phone = request.POST.get('phone')
			saveRecord.email = request.POST.get('email')
			saveRecord.sec_name = request.POST.get('sec_name')			
			saveRecord.save()
			messages.success(request, 'Edited successfully!')	
			return viewManager(request)
	else:
	 	display_table=Manager.objects.get(mgr_id=id)
	 	return render(request,"edit_manager.html",{'display_table':display_table})


def supply(request):
	if request.method == 'POST':
		if request.POST.get('supply_id') and request.POST.get('vendor_id') and request.POST.get('item_name') and request.POST.get('quantity'):
			saveRecord = Supply()
			saveRecord.supply_id = request.POST.get('supply_id')
			saveRecord.vendor_id = request.POST.get('vendor_id')
			saveRecord.item_name = request.POST.get('item_name')
			saveRecord.quantity = request.POST.get('quantity')	
			messages.success(request, 'Added successfully!')		
			saveRecord.save()
			return viewSupply(request)
	else: 
	     return render(request,'index_supply.html')



def viewSupply(request):
	supply_table=Supply.objects.all()
	return render(request,"view_supply.html",{'supply_table':supply_table})

def deleteSupply(request,id):
	supply_table=Supply.objects.get(supply_id=id)
	supply_table.delete()
	return viewSupply(request)

def editSupply(request,id):
	if request.method == 'POST':
		if request.POST.get('supply_id') and request.POST.get('vendor_id') and request.POST.get('item_name') and request.POST.get('quantity'):
			saveRecord = Supply()
			saveRecord.supply_id = request.POST.get('supply_id')
			saveRecord.vendor_id = request.POST.get('vendor_id')
			saveRecord.item_name = request.POST.get('item_name')
			saveRecord.quantity = request.POST.get('quantity')			
			saveRecord.save()
			messages.success(request, 'Edited successfully!')	
			return viewSupply(request)
	else:
	 	display_table=Supply.objects.get(supply_id=id)
	 	return render(request,"edit_supply.html",{'display_table':display_table})



def productInstance(request):
	if request.method == 'POST':
		if request.POST.get('prod_instance_id') and request.POST.get('sell_by_date') and request.POST.get('quantity') and request.POST.get('item_id'):
			saveRecord = Product_Instance()
			saveRecord.prod_instance_id = request.POST.get('prod_instance_id')
			saveRecord.sell_by_date = request.POST.get('sell_by_date')
			saveRecord.quantity = request.POST.get('quantity')			
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.save()
			messages.success(request, 'Added successfully!')
			return viewProductInstance(request)
	else: 
	     return render(request,'index_productInstance.html')



def viewProductInstance(request):
	product_table=Product_Instance.objects.all()
	return render(request,"view_product.html",{'product_table':product_table})

def deleteProductInstance(request,id):
	product_table=Product_Instance.objects.get(prod_instance_id=id)
	product_table.delete()
	return viewProductInstance(request)

def editProductInstance(request,id):
	if request.method == 'POST':
		if request.POST.get('prod_instance_id') and request.POST.get('sell_by_date') and request.POST.get('quantity') and request.POST.get('item_id'):
			saveRecord = Product_Instance()
			saveRecord.prod_instance_id = request.POST.get('prod_instance_id')
			saveRecord.sell_by_date = request.POST.get('sell_by_date')
			saveRecord.quantity = request.POST.get('quantity')			
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.save()
			messages.success(request, 'Edited successfully!')				
			return viewProductInstance(request)
	else:
	 	display_table=Product_Instance.objects.get(prod_instance_id=id)
	 	return render(request,"edit_product.html",{'display_table':display_table})



def Discard(request):
	if request.method == 'POST':
		if request.POST.get('date_discarded')  and request.POST.get('discard_id') and request.POST.get('item_id'):
			saveRecord = Discarded_Products()
			saveRecord.date_discarded = request.POST.get('date_discarded')
			# saveRecord.quantity = request.POST.get('quantity')
			saveRecord.discard_id = request.POST.get('discard_id')
			saveRecord.item_id = request.POST.get('item_id')
				
			saveRecord.save()
			messages.success(request, 'Added successfully!')
			return viewdiscard(request)
	else: 
	     return render(request,'index_discard.html')



def viewdiscard(request):
	discard_table=Discarded_Products.objects.all()
	return render(request,"view_discard.html",{'discard_table':discard_table})

def deletediscard(request,id):
	discard_table=Discarded_Products.objects.get(discard_id=id)
	discard_table.delete()
	return viewdiscard(request)

def editdiscard(request,id):
	if request.method == 'POST':
		if request.POST.get('date_discarded')  and request.POST.get('discard_id') and request.POST.get('item_id'):
			saveRecord = Discarded_Products()
			saveRecord.date_discarded = request.POST.get('date_discarded')
			# saveRecord.quantity = request.POST.get('quantity')
			saveRecord.discard_id = request.POST.get('discard_id')
			saveRecord.item_id = request.POST.get('item_id')
				
			saveRecord.save()
			messages.success(request, 'Edited successfully!')	
			return viewdiscard(request)
	else:
	 	display_table=Discarded_Products.objects.get(discard_id=id)
	 	return render(request,"edit_discard.html",{'display_table':display_table})




def viewCategory(request):
	category_table=Category.objects.all()
	return render(request,"view_category.html",{'category_table':category_table})

def deleteCategory(request,id):
	category_table=Category.objects.get(item_id=id)
	category_table.delete()
	return viewCategory(request)

def editCategory(request,id):
	if request.method == 'POST':
		if request.POST.get('item_id') and request.POST.get('ca_id') and request.POST.get('sec_name'):
			saveRecord = Category()
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.ca_id = request.POST.get('ca_id')
			saveRecord.sec_name = request.POST.get('sec_name')
		
			saveRecord.save()
			messages.success(request, 'Edited successfully!')			
			return viewCategory(request)	

	else:
	 	display_table=Category.objects.get(item_id=id)
	 	return render(request,"edit_category.html",{'display_table':display_table})


def category(request):
	if request.method == 'POST':
		if request.POST.get('item_id') and request.POST.get('ca_id') and request.POST.get('sec_name'):
			saveRecord = Category()
			saveRecord.item_id = request.POST.get('item_id')
			saveRecord.ca_id = request.POST.get('ca_id')
			saveRecord.sec_name = request.POST.get('sec_name')
			saveRecord.save()
			messages.success(request, 'Added successfully!')
			return viewCategory(request)
	else: 
	     return render(request,'index_category.html')



def SQLqueries(request):
	sql ="SELECT * FROM items where price>=1000"
	posts=Items.objects.raw(sql)
	print(posts)
	return render(request,'output.html',{'data':posts})






















# def purchase(request):
# 	if request.method == 'POST':
# 		if request.POST.get('quantity') and request.POST.get('item_id') and request.POST.get('vendor_id') and request.POST.get('order_date') and request.POST.get('mgr_id'):
# 			saveRecord = pur_order()
# 			saveRecord.quantity = request.POST.get('quantity')
# 			saveRecord.item_id = request.POST.get('item_id')
# 			saveRecord.vendor_id = request.POST.get('vendor_id')			
# 			saveRecord.order_date = request.POST.get('order_date')
# 			saveRecord.mgr_id = request.POST.get('mgr_id')			
# 			saveRecord.save()
# 			return viewpurchase(request)
# 	else: 
# 	     return render(request,'index_purchase.html')



# def viewpurchase(request):
# 	purchase_table=pur_order.objects.all()
# 	return render(request,"view_purchase.html",{'purchase_table':purchase_table})

# def deletepurchase(request,id1,id2):
# 	purchase_table=pur_order.objects.get(unique_together=id)
# 	purchase_table.delete()
# 	return viewpurchase(request)

# def editpurchase(request,id1, id2):
# 	if request.method == 'POST':
# 		if request.POST.get('quantity') and request.POST.get('item_id') and request.POST.get('vendor_id') and request.POST.get('order_date') and request.POST.get('mgr_id'):
# 			saveRecord = pur_order()
# 			saveRecord.quantity = request.POST.get('quantity')
# 			saveRecord.item_id = request.POST.get('item_id')
# 			saveRecord.vendor_id = request.POST.get('vendor_id')			
# 			saveRecord.order_date = request.POST.get('order_date')
# 			saveRecord.mgr_id = request.POST.get('mgr_id')			
# 			saveRecord.save()
# 			return viewpurchase(request)
# 	else:
# 	 	display_table=pur_order.objects.get(unique_together=(id1, id2))
# 	 	return render(request,"edit_purchase.html",{'display_table':display_table})


