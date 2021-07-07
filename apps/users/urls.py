from apps.users.views import ListViews
from django.urls import path

app_name='users'

urlpatterns = [
    path('',ListViews.as_view(), name='List'),
]