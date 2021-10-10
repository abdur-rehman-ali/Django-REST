from django.urls import path
from . import views

urlpatterns = [
    path('crud/',views.crudAPI.as_view()),
    path('crud/<int:pk>',views.crudAPI.as_view())
]
