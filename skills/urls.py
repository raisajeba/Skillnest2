from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'skill/<int:pk>/',
        views.skill_detail,
        name='skill_detail'
    ),
]
