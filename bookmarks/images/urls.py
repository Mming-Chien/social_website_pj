from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
	# url for retrieve and saving images
	path('create/', views.image_create, name='create'),
	# url for detail of the image
	path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
	# url for the like button
	path('like/', views.image_like, name='like'),
	# Infinite paginator page
	path('', views.image_list, name='list'),
	# The most viewed iamges
	path('ranking/', views.image_ranking, name='ranking'),
]