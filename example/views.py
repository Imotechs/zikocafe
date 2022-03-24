import genericpath
from time import time
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth. mixins import UserPassesTestMixin,LoginRequiredMixin
from example.forms import UserPostForm
from django.views.generic import CreateView
from django.contrib import messages
from example.templates.example.forms import UserRegistrationForm
from .models import  Job, Post,Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
# class TodoView(CreateView):
#     model = Post
#     fields = ['name']
#     success_url = '/'
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.save
#         return super().form_valid(form)



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


@csrf_exempt
def delete_todo(request,todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect('/')


class AddJobView(UserPassesTestMixin,CreateView):
    model = Job
    fields = ['title', 'price']
   
        
    def test_func(self):
        if User.is_superuser:
            return True
        return False

class UserAddPaymentView(LoginRequiredMixin,CreateView):
    model = Job
    fields = ['title','description', 'price']
    def form_valid(self, *args, **kwargs):
            self.customer ==request.user.username
            return super().form_valid(*args, **kwargs)

            
def allPaymentView(request,pk,*args, **kwargs):
    if request.method =='POST':
        job_id = pk
        job = Job.objects.filter(id = job_id)
        print('primary key :'+ str(pk))
    return render(request,  'payment/allpayments.html', {'job':job})

def about(request):

    return render(request, 'example/about.html')