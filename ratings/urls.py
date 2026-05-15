from django.urls import path
from . import views

urlpatterns = [
    path('rate/<int:exchange_id>/', views.submit_rating, name='submit_rating'),
    path('my-ratings/', views.user_ratings, name='user_ratings'),
]
