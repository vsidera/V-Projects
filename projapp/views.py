from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (DetailView, UpdateView, DeleteView)
from .forms import uploadForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'projapp/home.html', context)

class PostDetailView(DetailView):
    model = Post

@login_required(login_url='/login/')
def new_post(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('projapp-home')
    else:
        form = uploadForm()
    return render(request, 'projapp/post_form.html', {'form':form})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.profile.user:
            return True
        return False

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'projapp/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projapp/search.html',{"message":message})        
