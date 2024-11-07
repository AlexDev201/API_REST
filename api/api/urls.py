from rest_framework import routers
from . import views
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)  # Confirma que esté bien escrito

urlpatterns = [
    path('', include(router.urls)),
]