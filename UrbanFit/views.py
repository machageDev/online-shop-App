from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, 'login.html')  # or 'UrbanFit/login.html' if inside app folder
def navbar(request):
    return render(request,'navbar.html')
def home(request):
    return render(request,'home.html')
def forgot_password(request):
    return render(request,'forgot_password.html')
def register(request):
    return render(request,'register.html')