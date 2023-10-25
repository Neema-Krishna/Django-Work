from django.urls import path
from . import views

urlpatterns=[
    # path("january", views.index),
    path("challenges",views.indexi,name='index'),
    path('<int:month>',views.monthly_challeenges_bynumbers),
    path("<str:month>", views.monthly_challanges_1,name='monthly')
]