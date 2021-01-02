from django import forms
from supermarket_app.models import Vendor,Manager,Items,Stocks,Supply,Product_Instance,Discarded_Products,Category
class VendorForm(forms.ModelForm):
	class Meta:
		model=Vendor
		fields="__all__"

class ManagerForm(forms.ModelForm):
	class Meta:
		model=Manager
		fields="__all__"

class ItemsForm(forms.ModelForm):
	class Meta:
		model=Items
		fields="__all__"

class StocksForm(forms.ModelForm):
	class Meta:
		model=Stocks
		fields="__all__"

class SupplyForm(forms.ModelForm):
	class Meta:
		model=Supply
		fields="__all__"

class ProductInstanceForm(forms.ModelForm):
	class Meta:
		model=Product_Instance
		fields="__all__"

class DiscardForm(forms.ModelForm):
	class Meta:
		model=Discarded_Products
		fields="__all__"

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields="__all__"
# class PurchaseForm(forms.ModelForm):
# 	class Meta:
# 		model=pur_order
# 		fields="__all__"