from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .models import *

def index(request):
    return render(request, 'main.html')

# Products
def search_products(request):
    if request.method == 'GET':
        form = GetProductForm(request.GET)
        name = request.GET.get('name')
        if name:
            products = Product.objects.filter(name__icontains=name)
            
            return render(request, "get_form.html", {'form': form, 'name': 'producto', 'action': '/search-products/', 'object_list': products})
        else:
            form = GetProductForm()

    return render(request, "get_form.html", {'form': form, 'name': 'producto', 'action': '/search-products/'})
    
def save_product(request):
    if request.method == 'POST':
        form = PostProductForm(request.POST)
        if form.is_valid():
            product = Product(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                price = form.cleaned_data['price']
            )
            product.save()
            
            return HttpResponse('Producto guardado')
    else:
        form = PostProductForm()

    return render(request, 'post_form.html', {'form': form, 'name': 'producto', 'action': '/save-product/'})

# Categories
def search_categories(request):
    if request.method == 'GET':
        form = GetCategoryForm(request.GET)
        name = request.GET.get('name')
        if name:
            categories = Category.objects.filter(name__icontains=name)
            
            return render(request, "get_form.html", {'form': form, 'name': 'categoría', 'action': '/search-categories/', 'object_list': categories})
        else:
            form = GetCategoryForm()

    return render(request, "get_form.html", {'form': form, 'name': 'categoría', 'action': '/search-categories/'})
    
def save_category(request):
    if request.method == 'POST':
        form = PostCategoryForm(request.POST)
        if form.is_valid():
            category = Category(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
            )
            category.save()
            
            return HttpResponse('Categoría guardada')
    else:
        form = PostCategoryForm()

    return render(request, 'post_form.html', {'form': form, 'name': 'categoría', 'action': '/save-category/'})

# Orders
def search_orders(request):
    if request.method == 'GET':
        form = GetOrdersForm(request.GET)
        number = request.GET.get('number')
        if number:
            orders = Order.objects.filter(number=number)
            
            return render(request, "get_form.html", {'form': form, 'name': 'órden', 'action': '/search-orders/', 'object_list': orders})
        else:
            form = GetOrdersForm()

    return render(request, "get_form.html", {'form': form, 'name': 'órden', 'action': '/search-orders/'})
    
def save_order(request):
    if request.method == 'POST':
        form = PostOrderForm(request.POST)
        if form.is_valid():
            order = Order(
                number = form.cleaned_data['number'],
                total = form.cleaned_data['total']
            )
            order.save()
            
            return HttpResponse('Órden guardada')
    else:
        form = PostOrderForm()

    return render(request, 'post_form.html', {'form': form, 'name': 'órden', 'action': '/save-order/'})
