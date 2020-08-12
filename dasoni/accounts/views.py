from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        # print(request.POST)
        # print(form.is_valid())
        # print(form.error_messages)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_http_methods(['POST',])
def logout(request):
    auth_logout(request)
    return redirect('index')


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다!')
            return redirect('accounts:profile', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
        context={
            'form':form,
        }
    return render(request, 'accounts/password.html', context)


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(
            request.POST, instance=request.user
            )
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)