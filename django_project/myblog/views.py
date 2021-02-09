from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
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

def home(request):  # templates home html
    # post from database, to be passed as dict.
    context = {
        'posts': Post.objects.all()
    }
    return render (request, 'myblog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'myblog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order by date posted. Latest on top.
    paginate_by = 4 # Number of posts / page.

# List post of indivudual users.
class UserPostListView(ListView):
    model = Post
    template_name = 'myblog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4
    
    # To get username from url.
    def get_queryset(self):
        # get_object_or_404 - dispaly user posts or 404 error.
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # To forbid, when current user makes change to other author post.
    def test_func(self): 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render (request, 'myblog/about.html', {'title' : 'About'})
