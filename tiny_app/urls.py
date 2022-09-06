from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('libraries/', views.LibraryList.as_view(), name='library_list'),
    path('libraries/<int:pk>/', views.LibraryDetail.as_view(), name='library_detail')


]