from django.urls import path

from project_name.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
