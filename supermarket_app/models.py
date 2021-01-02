from django.forms import ModelForm, Textarea
from django.db import models



class Vendor(models.Model):
	vendor_id=models.IntegerField(primary_key=True)
	location=models.CharField(max_length=50)
	company_name=models.CharField(max_length=25)
	phone_no=models.CharField(max_length=10)
	email=models.EmailField(max_length=150)
	class Meta:
		db_table="vendor"

class Manager(models.Model):
	mgr_id=models.IntegerField(primary_key=True)
	mgr_name=models.CharField(max_length=20)
	phone=models.CharField(max_length=10)
	email=models.EmailField(max_length=150)
	sec_name=models.CharField(max_length=20)
	class Meta:
		db_table="Manager"

class Items(models.Model):
	item_id=models.IntegerField(primary_key=True)
	price=models.DecimalField(max_digits=7,decimal_places=2)
	item_name=models.CharField(max_length=50)
	brand=models.CharField(max_length=50)
	class Meta:
		db_table="Items"	

class Stocks(models.Model):
	item=models.ForeignKey(Items, on_delete=models.CASCADE)
	stock_id=models.IntegerField(primary_key=True)
	sec_name=models.CharField(max_length=20)
	quantity=models.IntegerField()
	unit_price=models.DecimalField(max_digits=7,decimal_places=2)
	total_price=models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		db_table="Stocks"

class Supply(models.Model):
	supply_id=models.IntegerField(primary_key=True)
	vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
	item_name=models.CharField(max_length=20)
	quantity=models.IntegerField()
    
	class Meta:
		db_table="Supply"
		
class Product_Instance(models.Model):
	prod_instance_id=models.IntegerField(primary_key=True)
	sell_by_date=models.DateField()
	quantity=models.IntegerField()
	item=models.ForeignKey(Items, on_delete=models.CASCADE)
    
	class Meta:
		db_table="Product_Instance"


class Discarded_Products(models.Model):
	date_discarded=models.DateField()
	# quantity=models.IntegerField()
	discard_id=models.IntegerField(primary_key=True)
	item=models.ForeignKey(Items, on_delete=models.CASCADE)

	class Meta:
		db_table="Discarded_Products"



class Category(models.Model):
	item_id=models.IntegerField(primary_key=True)
	ca_id=models.IntegerField()
	sec_name=models.CharField(max_length=20)
	
    
	class Meta:
		db_table="Category"





# class pur_order(models.Model):
# 	quantity=models.IntegerField()
# 	item_id=models.ForeignKey('Items',on_delete=models.CASCADE)
# 	vendor_id=models.ForeignKey(Vendor, related_name='item_set')
# 	order_date=models.DateField()
# 	manager=models.ForeignKey(Manager, on_delete=models.CASCADE)
	
    
# 	class Meta:
# 		unique_together = (("item_id", "vendor_id"),)
# 		db_table="pur_order"