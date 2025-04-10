from django.urls import path
from .views import HomeView, ProductListView, CategoryListView, CategoryDetailView, product_search

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('search/', product_search, name='product_search'),
]
