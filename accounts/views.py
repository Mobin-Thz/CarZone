from django.shortcuts import render,redirect
from django.contrib import messages, auth
from .models import User
# Create your views here.

def login(request):


    data={

    }

    return render (request, 'accounts/login.html',data)



def register(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
               messages.error(request, 'Username already exists')
               return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email, password=password)

                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    auth.login(request, user)
                    messages.success(request, 'You are logged in')
                    return redirect('dashboard')


        else:
            messages.error(request,'passwords do not match')
            return redirect(request, 'accounts/register.html')

        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

    data={

    }

    return render (request, 'accounts/register.html',data)





def logout(request):

    return redirect('home')



def dashboard(request):


    data={

    }

    return render (request, 'accounts/dashboard.html',data)
