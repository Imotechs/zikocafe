from asyncio import exceptions
import genericpath
from logging import exception
from time import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth. mixins import UserPassesTestMixin,LoginRequiredMixin
from example.forms import UserPostForm
from django.views.generic import CreateView
from django.contrib import messages
from example.templates.example.forms import UserRegistrationForm
from .models import  Job, Post,Todo,Payment
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
from .import functions
def home(request):
    Todo_list = Job.objects.all().order_by('-date')
    return render(request, 'example/index.html', {'todo_list':Todo_list})

def Register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username','email')
            messages.success(request, f' Account for {username} was created!  Login Now')
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'example/login.html',{'form':form})


@csrf_exempt
def add_todo(request):
    c_date = timezone.now()
    contents = request.POST['contents']
    content = contents
    context = {
        'date':c_date,
        'contents':contents,
    }
    print(contents)
    created_obj = Todo.objects.create(date = c_date, text = content)
    

    return HttpResponseRedirect('/')

class CustomersAddView(LoginRequiredMixin,CreateView):
    model = Job
    fields = ['title','description','price']
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.customer = self.request.user
        obj.save()
        return super().form_valid(form)

def payHomeView(request):
    user = request.user
    try:
        context = Job.objects.filter(customer = user) 
        print(f' my context data{context}')
        if context.count()==0:
            return HttpResponse("<h1>You Do not have a Pending Transction</h1")
        return render(request, 'example/pay.html', {'context':context})
    except TypeError:
        return HttpResponse('<h3>AnonymousUser Must Login to check</h3>')

def makepay(request,**kwargs):
    user = kwargs.get(request.user)
    payment = Payment.objects.all()
    product = Job.objects.filter(id = user)
    payment.job = payment.filter(job__customer = user)
    payment.payment_id = functions.get_payment_id()
    context = {
        'job':payment.job,
        'payment_id':payment.payment_id,
        'product':product,

    }
    return render(request, 'example/paying.html', {'context':context})


@csrf_exempt
def delete_todo(request,todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect('/')


class AddJobView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Job
    fields = ['title', 'price']
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.customer = self.request.user
        obj.save()
        return super().form_valid(form)
        
    def test_func(self):
        if User.is_superuser:
            return True
        return False

class UserAddPaymentView(LoginRequiredMixin,CreateView):
    model = Job
    fields = ['title','description', 'price']
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.customer = self.request.user
        obj.save()
        return super().form_valid(form)

            
def allPaymentView(request,pk,*args, **kwargs):
    try:
        if request.method =='POST':
            _job_id = pk
            job = Payment.objects.filter(id =pk,is_id=True)
            if job:
                job_obj = Job.objects.filter(id = _job_id)

                print('primary key :'+ str(pk))
                payment = Payment.objects.filter(job_id = pk)
                return render(request,  'payment/allpayments.html', {'job':job_obj,'payments':payment})

            else:
                payment = Payment(job_id = pk,payment_id = functions.get_payment_id(),is_id = True )   
                payment.save()
                job_obj = Job.objects.filter(id = _job_id)
                return render(request,  'payment/allpayments.html', {'job':job_obj, 'context':payment})

        else:
            return  HttpResponse('<h3>Return to payment page pls</h3>')

    except Exception:
         return  HttpResponse('<h3>Error!, Try Again Pls</h3>')



def about(request):

    return render(request, 'example/about.html')