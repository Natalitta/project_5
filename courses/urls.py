from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    #path('add/', views.add_product, name='add_product'),
    #path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    #path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]