from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index),
    path('createTask',views.create_task)
]