from django.shortcuts import render
from models import Account, Note, Category
#from django.db.models import Sum
from django.db.models import Q
from forms import AddNoteForm, AddAccountForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	accounts = Account.objects.all()
	return render(request, 'bank/index.html', {"accounts": accounts})

def account(request, account_id):
	account = Account.objects.get(id=account_id)
	q = request.GET.get('q','')
	notes = Note.objects.filter(Q(description__icontains=q) | Q(category__name__icontains=q), account=account_id).order_by('timestamp')
	#total = Note.objects.filter(account=account_id).aggregate(Sum('amount'))
	total =  account.balance
	request.GET
	return render(request, 'bank/account.html', {"notes": notes, "total": total, "account": account})

def addaccount(request):
	if request.method == 'POST':
		form = AddAccountForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			account = Account(
				number = cd['number'],
				bank = cd['bank'],
				balance = cd['balance'],
				nominal = cd['nominal']
			)
			account.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = AddAccountForm()
	return render(request, 'bank/addaccount.html', {'form': form})

def addnote(request, account_id):
	if request.method == 'POST':
		account = Account.objects.get(id=account_id)
		form = AddNoteForm(request.POST)
		if form.is_valid():			
			cd = form.cleaned_data
			note = Note(
						amount = cd['amount'],
						timestamp = cd['timestamp'],
						description = cd['description'],
						category = cd['category'],
						account = account
						)
			note.save()			
			account.balance = account.balance + cd['amount']
			account.save()
			return HttpResponseRedirect(reverse('account', args=[account_id]))
	else:
		form = AddNoteForm()
	return render(request, 'bank/addnote.html', {'form': form})

def delnote(request, account_id, note_id):
	note = Note.objects.get(id=note_id)
	account = Account.objects.get(id=account_id)
	if request.method == 'POST':
		account.balance = account.balance - note.amount
		note.delete()
		account.save()
		return HttpResponseRedirect(reverse('account', args=[account_id]))		
	return render(request, 'bank/delnote.html', {"note": note, "account": account})

	