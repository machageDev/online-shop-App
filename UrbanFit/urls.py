from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('navbar',views.navbar,name='navbar'),
    path('register',views.register,name='register'),
    path('home',views.home, name = 'home'),
    path('products',views.product_listing,name='product_listing'),
]
