from movies.views import ActorViews, MovieViews
from django.urls import path

urlpatterns = [
    path('actor', ActorViews.as_view()),
    path('movie', MovieViews.as_view()),
]
