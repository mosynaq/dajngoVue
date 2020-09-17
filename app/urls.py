from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.SimpleRouter()
router = routers.DefaultRouter()

router.register("authors", views.AuthorViewSet)
router.register("works-of-art", views.WorkOfArtViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
