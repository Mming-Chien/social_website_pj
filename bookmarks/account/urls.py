from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
	#previous login url
	#path('login/', views.user_login, name='login'),
	#Login/Logout urls
#	path('login/', auth_views.LoginView.as_view(), name='login'),
#	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	# Change password urls
#	path('password-change/', auth_views.PasswordChangeView.as_view(), name='passowrd_change'),
#	path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), 
#						name='password_change_done'),

	# Reset password urls
#	path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#	path('passowrd-reset/done/', auth_views.PasswordResetDoneView.as_view(), 
#			name='password_reset_done'),
#	path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
#			name='password_reset_confirm'),
#	path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
#			name='password_reset_complete'),
	
	# Urls for authentication
	path('', include("django.contrib.auth.urls")),

	path('', views.dashboard, name='dashboard'),

	# Url for register
	path('register/', views.register, name='register'),

	# Url for editing profile
	path('edit/', views.edit, name='edit'),

	# Url for list of users
	path('users', views.user_list, name='user_list'),

	# Url for follow or unfollow button
	path('users/follow/', views.user_follow, name='user_follow'),

	# Url for user detail
	path('users/<username>/', views.user_detail, name='user_detail'),

	#favicon
	path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]