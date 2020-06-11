from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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
