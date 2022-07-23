from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Code
from .models import Solved
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User_details
from django.views.decorators.cache import cache_control
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    search_query = ''
    post = Code.objects.all()
    
    
    if request.method == 'POST':
        filter=request.POST.getlist('checks[]')
        if "2" in filter:
            if "1" in filter:
            
                post = Code.objects.all()
                return render(request,'home.html',{'post':post})
            data =  Solved.objects.filter(fk = request.user.id)
            if data is not None:
                post = Code.objects.filter(id__in = data.values_list('code_id',flat=True))
                return render(request,'home.html',{'post':post})
            post = Code.objects.filter(completed=True)  
            return render(request,'home.html',{'post':post})
        elif "1" in filter: 
            post = Solved.objects.filter(fk=request.user.id)
            return render(request,'home.html',{'post':post})
        
        
       
        elif request.POST.getlist('check[]'):
            post = Code.objects.filter(completed = False)
        else:
            post = Code.objects.all()

         
    if request.GET.get('search-query'):
        search_query = request.GET.get('search-query')
    
        post = Code.objects.all().filter(title__contains=search_query)
    
        return render(request,'home.html',{'post':post})
    return render(request,'home.html',{'post':post})


@login_required(login_url='/login')
def solved(request,id):
    show = Code.objects.filter(id=id)
    return render(request,'solved.html',{'show':show})  


def to_be_solved(request,id):
    # solve = Code.objects.filter(id=id)
    return render(request,'to_be_solved.html')

@login_required(login_url='/login')
def view_code(request,id):
    show = Code.objects.filter(id=id)
    return render(request,'view.html',{'show':show})

@login_required(login_url='/login')
def questions(request,id):
    quest = Code.objects.filter(id=id)
    return render(request,'questions.html',{'quest':quest})
   
   
# def mail(request):
#     subject = 'Thank you for registering'
#     message = 'Welcome to the site'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['rikde1999@gmail.com']
#     send_mail( subject, message, email_from, recipient_list )
    
#     return HttpResponse("<h1>Mail</h1>")
   
def login_user(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request,'Invalid credentials')
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,'Invalid Credentials')
        
    return render(request,'login.html')

# def Register(request):

#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         User.objects.create_user(name,email,password)
#         return redirect("/")
    
#     return render(request,'register.html')

def Register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # print(username,email,password)
        
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username Taken')  
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email Taken')
            return redirect('register')
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('login')
    
    
    return render(request,'register.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    logout(request)
    return redirect("/")

def profile(request):
    
    user1 = request.user.id
    user2 = User_details.objects.filter(fk = user1)
    print(user2)
    return render(request,'profile.html',{'user2':user2})

def delete_user(request):
    
    username = request.user.username
    post = User.objects.get(username=username)
    post.delete()
    return redirect("/")
