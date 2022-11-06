from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class LoginForm(forms.Form):
	''' Form for logging in'''
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	''' Form for registration '''
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username', 'first_name', 'email']

	def clean_password2(self):
		''' Check two passwords '''
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Password don\'t match.')
		return cd['password2']

	def clean_email(self):
		''' Prevent using existing email '''
		data = self.cleaned_data['email']
		if User.objects.filter(email=data).exists():
			raise forms.ValidationError('Email already in use.')
		return data 



class UserEditForm(forms.ModelForm):
	''' Form for editing user '''
	class Meta:
		model = User 
		fields = ['first_name', 'last_name', 'email']

	def clean_email(self):
		''' Prevent using existing email '''
		data = self.cleaned_data['email']
		qs = User.objects.exclude(id=self.instance.id).filter(email=data)
		if qs.exists():
			raise forms.ValidationError('Email already in use.')
		return data 

class ProfileEditForm(forms.ModelForm):
	''' Form for editing profile '''
	class Meta:
		model = Profile
		fields = ['date_of_birth', 'photo']

