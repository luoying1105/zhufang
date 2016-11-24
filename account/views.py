from .forms import LoginForm
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request):
    return render(request,
                  'shop/index.html',
                  {'section': 'dashboard'})

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
