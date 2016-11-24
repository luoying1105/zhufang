from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    apartment_layout = ApartmentLayout.objects.all()
    device = Device.objects.all()
    products = Product.objects.filter(available=True)  # 拿取已经上架的全部商品
    if category_slug:  # 我们将使用一个可选的category_slug参数可选的过滤产品给定的类别。
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'apartment_layout': apartment_layout,
                   'device': device,
                   'products': products})


@login_required
def dashboard(request, city_slug=None):
    city = City.objects.all()[:5]  # 只选前五个
    products = Product.objects.filter(available=True)  # 拿取已经上架的全部商品
    if city_slug:  # 我们将使用一个可选的category_slug参数可选的过滤产品给定的类别。
        city = get_object_or_404(City, slug=city_slug)
        products = products.filter(city_name=city)
    return render(request,
                  'shop/product/index.html',
                  {'section': 'dashboard',
                   'cities': city})


# 就是商品的详细信息页面
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
