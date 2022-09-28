from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfilesList.as_view(), name='home'),
    path('<slug:slug>/', views.PupilProfile.as_view(), name='profile_detail'),
]
