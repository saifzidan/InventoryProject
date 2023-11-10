from django.urls import path
from . import views
app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("staff/", views.staff, name="staff"),
    path("staff/detail/<int:pk>", views.staff_detail, name="staff_detail"),
    path("product/", views.product, name="product"),
    path("product/update/<int:pk>", views.product_update, name="product_update"),
    path("product/delete/<int:pk>", views.product_delete, name="product_delete"),
    path("order/", views.order, name="order"),
]
