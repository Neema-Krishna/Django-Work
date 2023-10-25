from django.urls import path,include
from user_app import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
     
    path('login/',views.LoginView.as_view(),name='login'),
    
    path('homepage/',views.HomepageView.as_view(),name='homepage'),
    
    path('about/',views.AboutView.as_view(),name='about'),
    
    # path('blog/',views.BlogView.as_view(),name='blog'),
    
    path('car/',views.CarView.as_view(),name='car'),
    
    path('car/sort/', views.SortCarView.as_view(), name='car-listing-sort'),
    
    # path('car/mileage/',views.FilterCarView.as_view(),name='car-listing-mileage'),
    
    path('contact/',views.ContactView.as_view(),name='contact'),
    
    # path('cartview/',views.CartView.as_view(),name='cart'),
    
    path('cartview/<int:car_id>/', views.CartView1.as_view(), name='carts'),
    path('cart', views.CartView.as_view(), name='cart'),
    
    
    path('getbrandmodels/',views.ModelsView.as_view(),name='getbrandmodels'),
    # path('searchcarbyname/',views.FilterCarView.as_view(),name='searchcarbyname'),
    
    

    
    # path('car-detail/',views.CarDetailView.as_view(),name='car-detail')
    
    
    
]
