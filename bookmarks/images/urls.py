from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
	# url for retrieve and saving images
	path('create/', views.image_create, name='create'),
	# url for detail of the image
	path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail')
]