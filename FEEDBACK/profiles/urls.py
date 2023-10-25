from django.urls import path
 
from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path('profileview/',views.Profilesview.as_view())
] 