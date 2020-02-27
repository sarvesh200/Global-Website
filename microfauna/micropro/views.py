from django.shortcuts import render
from micropro.forms import Userform,Userprofileinfo


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    render(request,'micropro.index.html')

@login_required
def user_logout(request):
    logout(request)
    HttpResponseRedirect(reverse('index'))

@login_required
def showspecial(request):
    HttpResponse("You have logged in successfully")




def register(request):
    registerd = False
    if request.method == 'POST':
        user_form = Userform(request.POST)
        profile_form = Userprofileinfoform(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']

            profile.save()
            registerd =True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = Userform()
        profile_form = Userprofileinfoform()
    render(request,'micropro/register.html',{'user_form':user_form,'profile_form':profile_form,'registerd':registerd})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone malicoius logged in")
            print("thay logged in with username:{} password:{}".format(username,password))
    else:
        return render(request,'micropro/login.html',{})
