from django.contrib.auth.forms import UserCreationForm
from django.db  import models

from example.models import Post

class UserPostForm(UserCreationForm):
    name = models.CharField(max_length=200)
    class Meta:
        model = Post
        fields = ['name']
    