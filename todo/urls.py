from django.urls import path, include
from rest_framework import routers

from .views import TodoMVS

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', include(router.urls))
]