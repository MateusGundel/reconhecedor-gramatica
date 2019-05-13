from django.urls import path
from web import views

urlpatterns = [
    path('home/', views.home_view),
    path('home/create_post/', views.create_post),
]