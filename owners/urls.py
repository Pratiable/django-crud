from owners.views import OwnersView, DogsView
from django.urls import path

urlpatterns = [
    path('owner', OwnersView.as_view()),
    path('dog', DogsView.as_view()),
]
