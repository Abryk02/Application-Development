from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Product

# Create your views here.
def home(request):
    records = Product.objects.all()

    # Check to see if the user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You're logged in!")
            return redirect('home')
        else:
            messages.success(request, "Oops! Please try logging in again...")
            redirect('home')
    else:        
        return render(request, 'home.html', {'records': records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out. See ya!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome to E-commerce Platform")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_product(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        customer_record = Product.objects.get(id=pk)
        return render(request, 'product.html', {'product_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view the page!")
        return redirect('home')
    
def delete_product(request, pk):
    if request.user.is_authenticated:
        delete_record = Product.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Product is deleted successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete the product!")
        return redirect('home')
    
def add_product(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_product = form.save()
				messages.success(request,  "Product is added successfully.")
				return redirect('home')
		return render(request, 'add_product.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to add the record!")
		return redirect('home')


def update_product(request, pk):
	if request.user.is_authenticated:
		current_record = Product.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request,  "Record is updated successfully.")
			return redirect('home')
		return render(request, 'update_product.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to update the record!")
		return redirect('home')