from django.shortcuts import render, redirect
from .forms import LoginForm, UserEditForm, ProfileEditForm, UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages

# no need to write this view, automatically handled by django.contrib.auth
# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         # request method is post
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             username = cd['username']
#             password = cd['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request,  user)
#                     return HttpResponse('Authentication successful.')
#                 else:
#                     return HttpResponse('User account disabled.')
#             else:
#                 return HttpResponse('Invalid Login Credentials.')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Cannot edit profile at the moment.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
