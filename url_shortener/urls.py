from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home_page),
    path('hello', views.helloWorld),
    path('task', views.task),
    path('analytics',views.analytics),
    path('<slug:customname>',views.redirect_url)
]
