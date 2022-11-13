from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
	# url for retrieve and saving images
	path('create/', views.image_create, name='create'),
]