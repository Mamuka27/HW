
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

from .models import Category, Product

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
