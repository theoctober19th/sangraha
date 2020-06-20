from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ImageCreateForm
from django.contrib import messages
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from commons.decorators import ajax_required
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


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_who_liked.add(request.user)
            else:
                image.users_who_liked.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            print(e)
            pass
    return JsonResponse({'status': 'ko'})
