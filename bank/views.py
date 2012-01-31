from django.shortcuts import render
from models import Account, Note, Category
#from django.db.models import Sum
from django.db.models import Q
from forms import AddNoteForm, AddAccountForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
	accounts = Account.objects.all()
	return render(request, 'bank/index.html', {"accounts": accounts})

@login_required
def account(request, account_id):		
	account = Account.objects.get(id=account_id)
	q = request.GET.get('q','')
	notes = Note.objects.filter(Q(description__icontains=q) | Q(category__name__icontains=q), account=account_id).order_by('timestamp').select_related()
	#total = Note.objects.filter(account=account_id).aggregate(Sum('amount'))
	total =  account.balance
	request.GET
	return render(request, 'bank/account.html', {"notes": notes, "total": total, "account": account})

@login_required	
def addaccount(request):
	form = AddAccountForm(request.POST or None)	
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
			
	return render(request, 'bank/addaccount.html', {'form': form})

@login_required
def addnote(request, account_id):
	form = AddNoteForm(request.POST or None)
	if request.method == 'POST':
		account = Account.objects.get(id=account_id)
		if form.is_valid():			
			form.save(account)
			return HttpResponseRedirect(reverse('account', args=[account_id]))
	return render(request, 'bank/addnote.html', {'form': form})

@login_required
def delnote(request, account_id, note_id):
	note = Note.objects.get(id=note_id)
	account = Account.objects.get(id=account_id)
	if request.method == 'POST':
		account.balance = account.balance - note.amount
		note.delete()
		account.save()
		return HttpResponseRedirect(reverse('account', args=[account_id]))		
	return render(request, 'bank/delnote.html', {"note": note, "account": account})

	