from django.shortcuts import render
from .models import Account


def UserList(request):
    users = Account.objects.all()
    return render(request,"accounts/userlist.html",{'users':users})