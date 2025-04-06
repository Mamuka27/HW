from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Product, Category

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(ListView):
    model = Product
    template_name = 'category_detail.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
