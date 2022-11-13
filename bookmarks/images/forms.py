from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests

class ImageCreateForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title', 'url', 'description']
		widgets = {'url':forms.HiddenInput,}

	def clean_url(self):
		url = self.cleaned_data['url']
		valid_extensions = ['jpg', 'jpeg', 'png']
		# get extension of url .jpg ...
		extension = url.rsplit('.',1)[1].lower()
		# Raise error if extension is invalid
		if extension not in valid_extensions:
			raise forms.ValidationError('The given url does not match valid image extension.')
		return url 

	def save(self, force_insert=False, force_update=False, commit=True):
		''' retrieve image file by url and save it to the file system'''
		image = super().save(commit=False)
		image_url = self.cleaned_data['url']
		name = slugify(image.title)
		extension = image_url.rsplit('.',1)[1].lower()
		image_name = f'{name}.{extension}'
		# Download image form the given url
		response = requests.get(image_url)
		image.image.save(image_name, ContentFile(response.content), save=False)
		if commit: #Only save when commit = true
			image.save()
		return image