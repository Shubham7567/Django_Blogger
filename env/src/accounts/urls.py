from django.urls import path
from .views import UserList


urlpatterns = [
    path('Userlist/',UserList,name="user_list"),
]