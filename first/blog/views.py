from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMs',
        'title' : 'Blogpost 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 1',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
