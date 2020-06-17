from django import forms
from .models import Image
from django.conf import settings
from urllib.request import urlopen, Request
from django.utils.text import slugify
from django.core.files.base import ContentFile


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = settings.VALID_IMAGE_EXTENSIONS
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'Extension of the image is not recognized.')
        return url

    def save(self, commit=True, force_insert=False, force_update=False):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = '{}.{}'.format(slugify(image.title), extension)

        request = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(request)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()
        return image
