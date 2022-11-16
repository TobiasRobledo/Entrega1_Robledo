from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('save-product/', views.save_product, name='save-product'),
    path('search-products/', views.search_products, name='search-products'),
    
    path('save-category/', views.save_category, name='save-category'),
    path('search-categories/', views.search_categories, name='search-categories'),
    
    path('save-order/', views.save_order, name='save-order'),
    path('search-orders/', views.search_orders, name='search-orders'),
]
