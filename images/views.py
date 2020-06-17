from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.contrib import messages
# Create your views here.


@login_required
def image_create(request):
    print('i reacehd here!')
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            messages.success(request, "Image created successfully.")
            return redirect('dashboard')
    else:
        form = ImageCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'form': form, 'section': 'images', })
