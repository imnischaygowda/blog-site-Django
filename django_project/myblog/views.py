from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'author': 'Nischay',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date_posted': 'January 28, 2021 '
#     }
# ]

# Create your views here.

def home(request):             # templates home html
    # post from database, to be passed as dict.
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'myblog/home.html', context)

def about(request):
    return render (request, 'myblog/about.html', {'title' : 'About'})
