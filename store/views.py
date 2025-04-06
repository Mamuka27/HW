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


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })



from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q

def product_search(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    products = Product.objects.all()
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(slug__icontains=query))
    if category_filter:
        products = products.filter(category__name=category_filter)
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)

    categories = Category.objects.all()
    return render(request, 'product_search.html', {
        'products': products,
        'categories': categories,
        'query': query,
    })
