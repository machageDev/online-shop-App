from pyexpat.errors import messages
from django.shortcuts import redirect, render

from UrbanFit.models import User

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
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email= request.POST.get('email')
        password = request.POST.get('pasowrd')
        
        if User.objects.filter(email=email).exist():
            messages.error(request,"Email already exits.")
            return redirect(register)
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            
        )
        user.save()
        messages.success(request,"user registered successfully")
        return redirect('login')
    return render(request,'register.html')
        
        
    