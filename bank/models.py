from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Account(models.Model):
    number = models.CharField('Account number', max_length=20)
    bank = models.CharField('Bank name', max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    nominal = models.CharField('Nominal', max_length=40)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.number


class Note(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    account = models.ForeignKey(Account)

    def __unicode__(self):
        return '#%i %s' % (int(self.id), self.description)

    def is_expense(self):
        return self.amount < 0

    def is_deposit(self):
        return self.is_expense()

	