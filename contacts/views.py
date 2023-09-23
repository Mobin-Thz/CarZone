from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def inquiry (request):
    if request.method =='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title= request.POST['car_title']
        city= request.POST['city']
        state= request.POST['state']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        user_id = request.POST['user_id']


        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(car_id=car_id,user_id=user_id,)

            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car.')
                return redirect('/car/'+car_id)

        contact = Contacts(car_id=car_id, car_title=car_title, user_id=user_id, 
        first_name=first_name, last_name=last_name, customer_need=customer_need,
        city=city, state=state, email=email, phone_number=phone_number, message=message)
        


        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New car inquiry",
            "You have a new inquiry for the car "+ car_title + 'please login ' ,
            "mobin.projects@gmail.com",
            [admin_email],
            fail_silently=False,
        )



        contact.save()
        messages.success(request,'Your request has been submit.')
        return redirect('/car/'+car_id)
    
