from products.forms import ProductForm
from django.shortcuts import render,get_object_or_404
from .models import Product
from django.urls import reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import CreateView,UpdateView,DeleteView
# Create your views here.

def product_list(request):
    search=''
    if request.GET.get('search'):
        search = request.GET.get('search')
    products=Product.objects.filter(name__icontains=search)
    
    page_number = request.GET.get('page')
    paginator = Paginator(products, 3) 
    page_obj = paginator.get_page(page_number)
    
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products/product_list.html",{
        "products":products,
        "page_obj":page_obj
    })

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request, "products/product_detail.html",{
        "product":product
    })

class AddProduct(CreateView):
    model=Product
    template_name="products/add_product.html"
    form_class=ProductForm

class UpdateProduct(UpdateView):
    model=Product
    template_name="products/update_product.html"
    form_class=ProductForm

class DeleteProduct(DeleteView):
    model=Product
    success_url=reverse_lazy('products')
