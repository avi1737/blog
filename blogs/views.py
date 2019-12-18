from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import post
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
from django.contrib.auth.models import User

def home(request):
    posts=post.objects.all()
    context={
    'posts':posts
    }
    context={ 'posts':posts }
    return render(request,'blogs/home.html',context)

def about(request):
    return render(request,'blogs/about.html')

class PostListView(ListView):
    model=post
    template_name='blogs/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by= 4

class PostDetailView(DetailView):
    model=post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
