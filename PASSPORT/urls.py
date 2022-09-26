from django.urls import path
from . import views


urlpatterns = [
    path('', views.PupilsList.as_view(), name='pupils')
]
