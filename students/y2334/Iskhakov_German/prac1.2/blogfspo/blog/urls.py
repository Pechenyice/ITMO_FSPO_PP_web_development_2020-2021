from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:id>/', views.detail),
]