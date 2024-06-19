from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_reservations, name='user_reservations'),
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]
