from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view
from .views import dashboard

urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', dashboard, name='dashboard'),
    # login / logout urls
    url(r'^login/$',
        auth_view.login,
        name='login'),
    url(r'^logout/$',
        auth_view.logout,
        name='logout'),
    url(r'^logout-then-login/$',
        auth_view.logout_then_login,
        name='logout_then_login'),
    # 改密码 urls
    url(r'^password-change/$',
        auth_view.password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        auth_view.password_change_done,
        name='password_change_done'),

    # 忘记密码
    url(r'^password-reset/$',
        auth_view.password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_view.password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_view.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_view.password_reset_complete,
        name='password_reset_complete'),

    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),

]
