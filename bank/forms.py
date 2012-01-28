from django import forms
from models import Account, Category
from datetime import datetime


class AddNoteForm(forms.Form):
	amount = forms.DecimalField(label='Amount', decimal_places=2, required=True)
	timestamp = forms.DateTimeField(label='Timestamp', initial=datetime.now)
	description = forms.CharField(widget=forms.Textarea, max_length=100)
	category =  forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='')
	account = forms.ModelChoiceField(queryset=Account.objects.all(), empty_label='')


class EditAccountForm(forms.Form):
	number = forms.CharField(label='Account number', max_length=20, required=True)
	bank = forms.CharField(label='Bank name', max_length=30)
	nominal = forms.CharField(max_length=40)
	

class AddAccountForm(forms.Form):
	number = forms.CharField(label='Number', max_length=20, required=True)
	bank = forms.CharField(label='Bank name', max_length=30)
	balance = forms.DecimalField(max_digits=9, decimal_places=2)
	nominal = forms.CharField(label='Nominal', max_length=40)
	
	def save(self):
		cd = self.cleaned_data
		account = Account(
			number = cd['number'],
			bank = cd['bank'],
			balance = cd['balance'],
			nominal = cd['nominal']
		)
		account.save()

	