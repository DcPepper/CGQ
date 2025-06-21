from django.urls import include, path

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'geo/<str:iso>/', views.GeophraphyView)

urlpatterns = [
    path("", include(router.urls))
]
