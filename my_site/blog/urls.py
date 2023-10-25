from django.urls import path
from . import views

urlpatterns = [
    path('',views.Starting_page.as_view(), name='starting_page'),
    path('posts',views.Posts.as_view(), name='posts'),
    path('posts/<slug:slug>' ,views.Post_detail.as_view(), name='post_detail'),
    path('readlater',views.ReadLaterView.as_view(),name='read-later') 
]