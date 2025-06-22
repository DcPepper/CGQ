from django.urls import include, path

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'geo', views.GeophraphyView)

urlpatterns = [
    path("", include(router.urls)),
    path("hello", views.hello_world, name="hello")
]
