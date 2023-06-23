from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'time'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



