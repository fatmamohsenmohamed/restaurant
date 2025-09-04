from django.urls import path
from . import views

urlpatterns = [
    path('displaying/', views.displaying, name="displaying"),   # Show all menu items
    path('add/', views.adding, name="adding"),       # Add a new item
    path('edit/<int:ids>/', views.editing, name="editing"),   # Edit an item
    path('delete/<int:ids>/', views.deleting, name="deleting"), # Delete an item
]
