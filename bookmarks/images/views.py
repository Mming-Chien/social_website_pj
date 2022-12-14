
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action
import redis

# Conect to redis
r = redis.Redis(host=settings.REDIS_HOST,
				port=settings.REDIS_PORT,
				db=settings.REDIS_DB)

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
			create_action(request.user, 'bookmarked image', new_image)
			messages.success(request, 'image added successfully')
			# Redirect to new created item detail view 
			return redirect(new_image.get_absolute_url())
	else:
		# Build form with data privided by the bookmarklet via GET
		form = ImageCreateForm(data=request.GET)
	return render(request, 'images/image/create.html', {'section':'images', 'form':form},)

def image_detail(request, id, slug):
	image = get_object_or_404(Image, id=id, slug=slug)
	# increment total views by 1	
	total_views = r.incr(f'image:{image.id}:views')
	# Increment image ranking by 1
	r.zincrby('image_ranking',1 ,image.id)
	return render(request, 'images/image/detail.html', {'section':'images', 
					'image':image, 'total_views': total_views})

@login_required
@require_POST
def image_like(request):
	image_id = request.POST.get('id')
	action = request.POST.get('action')
	if image_id and action:
		try:
			image=Image.objects.get(id=image_id)
			if action=='like':
				image.users_like.add(request.user)
				create_action(request.user, 'likes', image)
			else:
				image.users_like.remove(request.user)
			return JsonResponse({'status':'ok'})
		except Image.DoesNotExist:
			pass 
	return JsonResponse({'status':'error'})

@login_required
def image_list(request):
	''' infinite scroll, handle first page and scroll pages'''
	images = Image.objects.all()
	paginator = Paginator(images, 8)
	page = request.GET.get('page')
	images_only = request.GET.get('images_only')
	#images_only the flag to know the scroll pages
	try:
		images = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		images = paginator.page(1)
	except EmptyPage:
		if images_only:
			# If AJAX request and page out of range
			# return an empty page
			return HttpResponse('')
		# If page out of range return the last page of results
		images = paginator.page(paginator.num_pages)
	if images_only:
		# return for scroll page
		return render(request, 'images/image/list_images.html', 
			{'section':'images', 'images':images})
	# return for initial page
	return render(request, 'images/image/list.html', 
		{'section':'images', 'images':images})

@login_required
def image_ranking(request):
	# Get image ranking dictionary
	image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[:10]
	image_ranking_ids = [int(id) for id in image_ranking]
	# Get most viewed images
	most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
	most_viewed.sort(key=lambda x:image_ranking_ids.index(x.id))
	return render(request, 'images/image/ranking.html', {'section':'images', 'most_viewed':most_viewed})
