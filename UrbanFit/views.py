from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import Product
from django.core.paginator import Paginator

from UrbanFit.models import User

# Create your views here.


def login_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        user = authenticate(request, username=first_name, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('dashbaord')
        else:
            messages.error(request,"invalid credentialsa")
            return render(request,"login.html",{"error":"invalid credential"})
        return render(request,"login.html")
            
    
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
        
def product_listing(request):
    # Initialize filters with default values
    category_filter = request.GET.get('category', None)
    size_filter = request.GET.get('size', None)
    color_filter = request.GET.get('color', None)
    sort_by = request.GET.get('sort_by', 'name')  # default sorting by name
    
    products = Product.objects.all()
    
    # Apply filters
    if category_filter:
        products = products.filter(category=category_filter)
    
    if size_filter:
        products = products.filter(size=size_filter)
    
    if color_filter:
        products = products.filter(color=color_filter)
    
    # Apply sorting
    if sort_by == 'price':
        products = products.order_by('price')
    elif sort_by == 'newest':
        products = products.order_by('-id')  # assuming id is based on creation date
    elif sort_by == 'best-rated':
        products = products.order_by('-rating')  # assuming there's a 'rating' field
    
    # Pagination
    paginator = Paginator(products, 9)  # Show 9 products per page
    page = request.GET.get('page')
    paginated_products = paginator.get_page(page)
    
    context = {
        'products': paginated_products,
        'category_filter': category_filter,
        'size_filter': size_filter,
        'color_filter': color_filter,
        'sort_by': sort_by,
    }
    
    return render(request, 'product_listing.html', context)
                