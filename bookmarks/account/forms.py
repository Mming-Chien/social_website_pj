from django import forms

class LoginForm(forms.Form):
	''' Form for logging in'''
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)