from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
	''' View for create image form and handle image submision'''
	if request.method == 'POST':
		# Form submitted
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			#Form data is valid
			cd = form.cleaned_data
			new_image = form.save(commit=False)
			# asign current user to the item
			new_image.user = request.user 
			new_image.save()
			messages.success(request, 'image added successfully')
			# Redirect to new created item detail view 
			return redirect(new_image.get_absolute_url())
	else:
		# Build form with data privided by the bookmarklet via GET
		form = ImageCreateForm(data=request.GET)
	return render(request, 'images/image/create.html', {'section':'images', 'form':form},)