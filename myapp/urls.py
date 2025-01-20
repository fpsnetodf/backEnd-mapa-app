from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadastroViewSet

router = DefaultRouter()
router.register(r'cadastros', CadastroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
