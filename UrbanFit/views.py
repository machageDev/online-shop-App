from django.shortcuts import render

# Create your views here.


def login_view(request):
    return render(request, 'login.html')  # or 'UrbanFit/login.html' if inside app folder
def navbar(request):
    return render(request,'navbar.html')