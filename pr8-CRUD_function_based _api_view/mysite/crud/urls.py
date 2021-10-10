from django.urls import path
from . import views

urlpatterns = [
    path('crud/',views.crudAPI),
    path('crud/<int:pk>',views.crudAPI)
]
