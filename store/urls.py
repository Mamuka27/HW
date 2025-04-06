from django.urls import path
from .views import HomeView, ProductListView, CategoryListView, CategoryDetailView

app_name = 'shop'  

urlpatterns = [
<<<<<<< HEAD
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

=======
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('search/', views.product_search, name='product_search'),
>>>>>>> 821fd0c718e8e02ba5b1a3db13b7fe3d2aad1d90
]
