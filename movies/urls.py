# from django.urls import path, include
# from rest_framework import routers
# from movies.views import ActionViewSet
# from . import views

# router = routers.SimpleRouter()
# router.register(r"action", ActionViewSet)
# router.register(r"movies", views.MovieViewSet)

# urlpatterns = [path("", include(router.urls))]
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, ActionViewSet

router = routers.SimpleRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"action", ActionViewSet, basename="action")
router.register(r"comedy", MovieViewSet, basename="comedy")

urlpatterns = [
    path("", include(router.urls)),
]
