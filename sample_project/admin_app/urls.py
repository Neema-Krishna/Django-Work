from django.urls import path,include
from admin_app import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='indexadmin'),
    
]