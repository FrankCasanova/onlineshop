from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(aviable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  template_name='shop/product/list.html',
                  context={
                      'category': category,
                      'products': products,
                      'categories': categories,
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                aviable=True)

    return render(request,
                  template_name='shop/product/detail.html',
                  context={
                      'product': product
                  })
