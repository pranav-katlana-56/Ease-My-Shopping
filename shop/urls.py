from django.urls import path, include
from django.contrib import admin
from shop import views

admin.site.site_header = 'EASE MY SHOPPING'
admin.site.site_title = 'EASE MY SHOPPING'
admin.site.index_title = 'EASE MY SHOPPING'

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('products', views.product),
    path('productview/<int:myid>/<int:price>' , views.productview),
    path('productview/<int:myid>/orderforme' , views.orderforme),
    path('gadgets', views.gadgets),
    path('cashback',views.cashbackform),
    path('search' , views.search),
    path('specifications/<int:myid>/<int:Price>/' , views.specification),
    path('flipkart' , views.flipkart),
    path('sucess' , views.sucess),
    path("contactus", views.contact),
    path("message", views.message),
    path("trending", views.trending)
    
]
