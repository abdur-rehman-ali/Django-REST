from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentAPI,name='studentAPI'),
    path('list/',views.studentAPIList,name='studentAPIList'),
]