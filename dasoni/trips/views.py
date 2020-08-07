from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def share(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request,'trips/share.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('trips:share')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'trips/share_create.html', context)