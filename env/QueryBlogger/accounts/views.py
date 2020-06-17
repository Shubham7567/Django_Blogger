from django.shortcuts import render

# Create your views here.
def userview(request):
    return render(request,'accounts/list.html')