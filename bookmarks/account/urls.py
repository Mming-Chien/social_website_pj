from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

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



]