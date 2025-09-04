from django.urls import path

from .views import *

urlpatterns = [
    path("customer_list/",customer_list,name="customer_list"),
    path("detailsandorder/<int:customer_id>/",customer_detail,name="customer_detail"),
    path("customer_add/",customer_add,name="customer_add"),
    path("customer_edit/<int:customer_id>/", customer_edit, name="customer_edit"),
    path("customer_delete/<int:customer_id>/", customer_delete, name="customer_delete"),

]