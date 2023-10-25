from django.urls import path
from .import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank_you',views.ThankyouView.as_view()),
    path('reviews',views.ReviewView1.as_view()),
    # path('reviews/favorite',views.Favorite.as_view()),
    path('reviews/<int:id>',views.SingleReviewView.as_view(),name='SingleReviewView')
]