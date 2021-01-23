from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('Input/', views.Input, name='input'),
    path('modifyStudent/<str:pk>/', views.modifyStudent, name='modifyStudent'),
    path('deleteStudent/<str:pk>/', views.deleteStudent, name='deleteStudent'),
    path('studentView/', views.studentView, name='studentView'),
]