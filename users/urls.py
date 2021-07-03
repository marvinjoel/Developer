from users.views import ListViews
from django.urls import path

urlpatterns = [
    path('', ListViews.as_view(), name='list'),
]