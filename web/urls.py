from django.urls import path
from web import views

urlpatterns = [
    path('', views.home_view),
    path('create_post/', views.create_post),
]