from django.urls import path
from django.urls import include

from rest_framework import routers

from project_name.api.auth.views import LoginViewSet

app_name = 'api.v1'

router = routers.SimpleRouter()

urlpatterns = [
    path('login/', LoginViewSet.as_view({'post': 'post'}), name='login'),

    path('', include(router.urls)),
]
