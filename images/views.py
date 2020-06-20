from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.contrib import messages
from .models import Image
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
            return redirect(image.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
    return render(request, 'images/image/create.html', {'form': form, 'section': 'images', })


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', context={'image': image, 'section': 'images'})
