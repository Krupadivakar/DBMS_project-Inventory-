"""supermarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from supermarket_app import views
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainScreen/', views.mainScreen, name = 'mainScreen'),


    path('supmk/',views.supmk, name = 'vendor'),
    path('viewVendor/',views.viewVendor,name='Vendor Table') ,
    path('editVendor/<int:id>',views.editVendor,name='Edit Vendor'), 
    path('deleteVendor/<int:id>',views.deleteVendor,name='Delete Vendor'), 


    path('Discard/',views.Discard, name = 'discard'),
    path('viewdiscard/',views.viewdiscard,name='Discard Product Table') ,
    path('editdiscard/<int:id>',views.editdiscard,name='Edit Discard Product'), 
    path('deletediscard/<int:id>',views.deletediscard,name='Delete Discard Product '), 


    path('productInstance/',views.productInstance, name = 'product'),
    path('viewProductInstance/',views.viewProductInstance,name='Product Instance Table') ,
    path('editProductInstance/<int:id>',views.editProductInstance,name='Edit Product Instance'), 
    path('deleteProductInstance/<int:id>',views.deleteProductInstance,name='Delete Product Instance'), 

    path('supply/',views.supply, name = 'supply'),
    path('viewSupply/',views.viewSupply,name='Supply Table') ,
    path('editSupply/<int:id>',views.editSupply,name='Edit Supply'), 
    path('deleteSupply/<int:id>',views.editSupply,name='Delete Supply'), 

 
    path('category/',views.category, name = 'category'),
    path('viewCategory/',views.viewCategory,name='Category Table') ,
    path('editCategory/<int:id>',views.editCategory,name='Edit Category'), 
    path('deleteCategory/<int:id>',views.deleteCategory,name='Delete Category'),    

    path('managerSupmk/',views.managerSupmk, name = 'manager'),
    path('viewManager/',views.viewManager,name='Manager Table') ,
    path('editManager/<int:id>',views.editManager,name='Edit Manager'), 
    path('deleteManager/<int:id>',views.deleteManager,name='Delete Manager'), 

    path('viewItems/',views.viewItems,name='View Table'),
    path('viewStocks/',views.viewStocks,name='Stocks Table'),
    path('itemsSupmk/',views.itemsSupmk,name='Items'),
    path('stocksSupmk/',views.stocksSupmk,name='Stocks'),
    path('editItem/<int:id>',views.editItem,name='Edit option'),
    path('deleteItem/<int:id>',views.deleteItem,name='Delete option'),

    path('Loginpage/',views.Loginpage,name='Loginpage'),
    path('SQLqueries/',views.SQLqueries,name='SQLqueries'),
     path('login/',views.login,name='login'),
    path('register/',views.register,name='register')
]
