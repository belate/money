from django.contrib import admin
from money.bank.models import Category, Account, Note

class AccountAdmin(admin.ModelAdmin):
	list_display = ('number', 'bank', 'balance')
	
class NoteAdmin(admin.ModelAdmin):
	list_display = ('amount', 'description', 'category', 'timestamp')
	ordering = ('timestamp',)
	
admin.site.register(Category)
admin.site.register(Account, AccountAdmin)
admin.site.register(Note, NoteAdmin)