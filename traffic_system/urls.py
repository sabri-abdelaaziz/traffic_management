from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
# Ajouter les autres routes

urlpatterns = [
    path('', include(router.urls)),
]
