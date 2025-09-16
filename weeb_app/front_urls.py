from django.urls import path
from .front_views import blog

urlpatterns = [
    path("blog/", blog, name="blog"),
]

