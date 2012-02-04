from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
	username = forms.CharField(label='User name', max_length=30, required=True)
	first_name = forms.CharField(label='First name', max_length=30)
	last_name = forms.CharField(label='Last name', max_length=30)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(), required=True)
	passwordTry = forms.CharField(widget=forms.PasswordInput(), label='Password again', required=True)
	
	def save(self):
		cd = self.cleaned_data
		user = User(
			username = cd['username'],
			first_name = cd['first_name'],
			last_name = cd['last_name'],
			email = cd['email'],
			password = cd['password']
		)
		user.set_password(cd['password'])
		user.save()
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).count():
			raise forms.ValidationError('Username is already use.')
		return username