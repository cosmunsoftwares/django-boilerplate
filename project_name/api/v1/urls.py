from django.urls import path
from django.urls import include

from rest_framework import routers

from project_name.api.v1.auth import views as auth_views

app_name = 'api.v1'

router = routers.SimpleRouter()

urlpatterns = [
    path('login/', auth_views.LoginViewSet.as_view({'post': 'post'}), name='login'),

    path('', include(router.urls)),
]
