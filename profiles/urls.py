from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:course_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]