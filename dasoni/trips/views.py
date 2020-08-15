from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def spotchart(request):
    return render(request, 'trips/spotchart.html')


def share(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request,'trips/share.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('trips:photo')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'trips/share_create.html', context)


def dasonitour(request):
    return render(request,'trips/dasonitour.html')


def photo(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'trips/photo.html', context)


def social(request):
    return render(request, 'trips/social.html')