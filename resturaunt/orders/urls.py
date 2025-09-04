from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.creating, name="creating"),
    path('add/<int:order_id>/', views.addingItems, name="addingItems"),
    path('display/<int:order_id>/', views.displaying, name="displaying"),
]
