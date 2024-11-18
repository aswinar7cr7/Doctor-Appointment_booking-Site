from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

from.forms import CustomerForm


# Create your views here.


@login_required
def home (request):
    form=CustomerForm()
    return render (request,'home.html', {'myform': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form,})



def forgot_password(request):
    return render(request, 'forgotpwd.html')

def loginview(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    user=authenticate(request,username=uname,password=pwd)
    if user is not None:
        login (request,user)
        return redirect('home')
    else:
        return render (request,'login.html',{'myform':'No User Found'})
    



def addcontact(request):
    try:
        if request.method == 'POST':
            custform = CustomerForm(request.POST)
            
            if custform.is_valid():
                # Check if the customer with the same date and time already exists
                date = custform.cleaned_data['date']
                time = custform.cleaned_data['time']
                
                # Check if a customer already exists with the same date and time
                if Customer.objects.filter(date=date, time=time).exists():
                    return render(request, 'home.html', {
                        'myform': custform, 
                        'msg': 'User with this Date and Time already exists.',
                        'error': True  # Flag to indicate an error
                    })
                else:
                    # Save the new customer if no conflict
                    custform.save()
                    return render(request, 'home.html', {
                        'myform': custform, 
                        'msg': 'User added successfully.',
                        'error': False  # No error
                    })
        else:
            custform = CustomerForm()
            
        return render(request, 'home.html', {'myform': custform, 'msg': '', 'error': False})

    except Exception as e:
        print(e)
        return render(request, 'home.html', {'msg': 'Cant add customer', 'error': True})

    

def logout_view(request):
    logout(request)
    return redirect('login')


def resetpassword(request):
    uname=request.POST['uname']
    newpwd=request.POST['password']
    try:
        user=User.objects.get(username=uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return redirect('login')
    except Exception as e:
        print(e)
        return render (request,'forgot.html',{'msg':'Passsowrd not reset'})
    

def views_bookings(request):
    all_customers = Customer.objects.all() 
    return render(request, 'bookings.html', {'customers': all_customers})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import Customer
import json

@csrf_exempt  # To exempt CSRF verification for this specific view (you can also apply CSRF token handling in your JS)
def delete_booking(request, booking_id):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user with username and password
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                # Retrieve the customer booking to delete
                booking = Customer.objects.get(id=booking_id, user=user)

                # Delete the booking
                booking.delete()

                return JsonResponse({'success': True})
            except Customer.DoesNotExist:
                return JsonResponse({'error': 'Booking not found or you do not have permission to delete it.'})
        else:
            return JsonResponse({'error': 'Authentication failed. Please check your credentials.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)



from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import Customer
import json

@csrf_exempt
def update_booking(request, booking_id):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        new_date = data.get('new_date')
        new_time = data.get('new_time')

        # Authenticate the user with username and password
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                # Retrieve the customer booking to update
                booking = Customer.objects.get(id=booking_id, user=user)

                # Update the date and time
                booking.date = new_date
                booking.time = new_time
                booking.save()

                return JsonResponse({'success': True})
            except Customer.DoesNotExist:
                return JsonResponse({'error': 'Booking not found or you do not have permission to update it.'})
        else:
            return JsonResponse({'error': 'Authentication failed. Please check your credentials.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
