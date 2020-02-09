from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse, Http404

from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth
from django.contrib.auth.models import Permission, User


from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .forms import GymCreate, TrainerForm, AbcForm, MemberForm, PaymentForm
from gymapp.models import Gym, Trainer, Members, abc, Payment



def index(request):
    shelf = Gym.objects.all()
    return render(request, 'gymapp/CRUD/premium.htm', {'shelf': shelf})

    
def upload(request):
    upload = GymCreate()
    if request.method == 'POST':
        upload = GymCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid!!")
    else:
        return render(request, 'gymapp/CRUD/upload_form.htm', {'upload_form':upload})
           
def update_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    gym_form = GymCreate(request.POST or None, instance = values)
    if gym_form.is_valid():
       gym_form.save()
       return redirect('index')
    return render(request, 'gymapp/CRUD/upload_form.htm', {'upload_form':gym_form})

def delete_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    values.delete()
    return redirect('index')



"""
Search Functionality
"""

def search_function_hai(request):
    if request.method =='GET':
        finds = request.GET['hacsac']
        if finds:
            match = Gym.objects.filter(Q(workoutname__icontains=finds))                             
            if match:                
                return render(request,'gymapp/CRUD/premium.htm', {'sac':match})
            else:
                messages.error(request, "The word, You type did  not Exist")
        else:
            return HttpResponseRedict('gymapp/CRUD/premium.htm')  
    return render(request, 'gymapp/CRUD/premium.htm')         


def view_register_users(request):
    if request.method =="GET":
        return render(request,'Registration/signup.htm')
    else:

        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
        user.save()
        return render(request,'login/home.htm')
        return HttpResponse("Signup Successful")
        return redirect('/')


def view_authenticate_users(request):
    if request.method =="GET":
            return render (request,'Login/login.htm')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return render(request,"additionalhtml/access.htm")
        else:
            return render(request, 'Login/login.htm')


def logout(request):
    auth.logout(request)   
    return render(request,'login/login.htm')

def view_accesspage_by_authorized_user(request):
    if request.user.is_authenticated:
        return render(request, "additionalhtml/access.htm")
    else:
        return HttpResponse("Error, Please Register First!!!")


def contact(request):
    return render(request,'gymapp/Navbar/contact.htm')      


def home(request):
  return render(request,'login/home.htm')

def course(request):
    return render(request,'gymapp/NavBar/course.htm')

def singuppage(request):
    return render(request,'registration/signup.htm')

def accesspage(request):
    return render(request,'additionalhtml/access.htm')

def schedulepage(request):
    return render(request,'gymapp/NavBar/schedule.htm')

def trainderdet(request):
    return render(request,'gymapp/NavBar/trainerdet.htm')


# def trainer_create_form(request):
#     form = TrainerForm(request.POST)
#     if form.is_valid():
#         form.save()
#     context ={
#         'form':form
#     }    
#     return render(request, 'gymapp/Model/trainer.htm', context)


def trainer_create_form(request):
    if request.method =='POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            sav = form.save()
        return HttpResponse("Data is Successfully Saved")    
        # return render(request, 'gymapp/Model/trainer.htm') 
    else:
        form = TrainerForm()  
        return render(request, 'gymapp/Model/trainer.htm', {'form': form}) 


def abc_create_form(request):
    form1 = AbcForm(request.POST)
    if form1.is_valid():
        form1.save()
    store_context = {
        'store':form1
    }
    return render(request,'gymapp/Model/abc.htm', store_context)    


def members_create_form(request):
    form2 = MemberForm(request.POST)
    if form2.is_valid():
        form2.save()
    context={
        'form2':form2
    }
    return render(request,'gymapp/Model/members.htm',context)

    
def Payment_create_form(request):
    form3 = PaymentForm(request.POST)
    if form3.is_valid():
        form3.save()
    context={
        'form3':form3
    }
    return render(request,'gymapp/Model/payment.htm', context)

