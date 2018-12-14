from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,\
    update_session_auth_hash
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from movie.forms import UserForm,RegistrationForm
from movie.models import Customer
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
def index(request):
    return render(request,'index.html')
'''def aboutus(request):
    return render(request,'about-us.html')
def article(request):
    return render(request,'article.html')
def articles(request):
    return render(request,'articles.html')
def contactus(request):
    return render(request,'contact-us.html')
def sitemap(request):
    return render(request,'sitemap.html') '''
@login_required
def special(request):
    
    return HttpResponse("You are logged in!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def user_login(request):
    
    
    if request.method=='POST':

        
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user1=authenticate(username=username,password=password)
        
        if user1 is not None:
            
            if user1.is_authenticated:
                request.session['username']=username
                login(request,user1)
                return HttpResponseRedirect(reverse('index'))
            else:
                
                return HttpResponse("Account is not active")
        else:
            
            return HttpResponseRedirect(reverse('user_login'))
    else:
        
            return render(request,'login.html')
    
def register(request):
    
    registered=False
    
    if request.method =="POST":
        
        user_form=UserForm(data=request.POST)
        register_form=RegistrationForm(data=request.POST)
        
        if user_form.is_valid() and register_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            reg=register_form.save(commit=False)
            reg.user=user
            reg.save()
            registered=True
            subject='Thankyou for registering'
            message='Welcome to Cinema World'
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email]
            send_mail(subject,message,from_email,to_list)
        else:
            print(user_form.errors,register_form.errors)
    else:
        
        user_form=UserForm()
        register_form=RegistrationForm()
    
    return render(request,'registration.html',{'user_form':user_form,'register_form':register_form,'registered':registered})  
@login_required
def user_profile(request):
    
    uname=request.session['username']
    customer=User.objects.filter(username=uname)
    return render(request,'user_profile.html',{'customer':customer})

class UserUpdate(UpdateView):
    fields=('first_name','last_name','username')
    model=User
    #form_class=UserForm
    template_name='user_update_form.html'
    success_url=reverse_lazy('index')
    def post(self, request, *args, **kwargs):
        request.session['username']=request.POST.get('username')
        return UpdateView.post(self, request, *args, **kwargs)
@login_required
def change_password(request):
    
    if request.method == 'POST':
        form =PasswordChangeForm(user=request.user,data=request.POST)
        success=False
        if form.is_valid():
            form.save()
            #form.save()
            success=True
            update_session_auth_hash(request,form.user)
            #messages.success(request,'Your password was successfully updated')
            return render(request,'change_password.html',{'success':success})
        else:
            messages.error(request,'Please correct the error below')
            form=PasswordChangeForm(user=request.user)
            
            return render(request,'change_password.html',{'forms':form,'success':success})
   
    
    else:
        form=PasswordChangeForm(user=request.user)
        
        return render(request,'change_password.html',{'forms':form})