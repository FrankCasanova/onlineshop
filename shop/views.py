from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category,
                                     translations__language_code=language,
                                     translations__slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  template_name='shop/product/list.html',
                  context={
                      'category': category,
                      'products': products,
                      'categories': categories,
                  })


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  template_name='shop/product/detail.html',
                  context={
                      'product': product,
                      'cart_product_form': cart_product_form
                  })
