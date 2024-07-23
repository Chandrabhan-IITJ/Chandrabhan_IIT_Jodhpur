from django.urls import path
from . import views

urlpatterns = [
    path('',views.greetUser, name='greetUser')
]
