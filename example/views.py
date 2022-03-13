import genericpath
from time import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from example.forms import UserPostForm
from django.views.generic import CreateView
from .models import Company, Post,Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
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
    Todo_list = Todo.objects.all().order_by('-date')
    return render(request, 'example/home.html', {'Todo_list':Todo_list})


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