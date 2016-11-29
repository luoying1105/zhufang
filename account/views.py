from .forms import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from shop.models import *
from .models import Profile

# Create your views here.
@login_required
def dashboard(request, city_slug=None):
    city = City.objects.all()[:5]  # 只选前五个
    products = Product.objects.filter(available=True)[:3]  # 拿取3个已经上架的全部商品
    campus = Campus.objects.all()[:3]
    if city_slug:  # 我们将使用一个可选的category_slug参数可选的过滤产品给定的类别。
        city = get_object_or_404(City, slug=city_slug)
        products = products.filter(city_name=city)
    return render(request,
                  'shop/product/index.html',
                  {'section': 'dashboard',
                   'cities': city,
                   'products': products,
                   'campus': campus
                   })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('登录成功')
                else:
                    return HttpResponse('该账户不存在')
        else:
            return HttpResponse('非法登录')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def register(request):
    user_form =  UserRegistrationForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            return render(request,
                      'account/register_done.html',
                      {'new_user': new_user})
        else:
           user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
   if request.method == 'GET':
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm()
   if request.method == 'POST':
       user_form = UserEditForm(instance=request.user,
                                data=request.POST)
       profile_form = ProfileEditForm(
           instance=request.user.profile,
           data=request.POST,
           files=request.FILES)
       if user_form.is_valid() and profile_form.is_valid():
           user_form.save()
           profile_form.save()
   else:
       user_form = UserEditForm(instance=request.user)
       profile_form = ProfileEditForm(
       instance=request.user.profile)
   return render(request,
                 'account/edit.html',
                 {'user_form': user_form,
                  'profile_form': profile_form})