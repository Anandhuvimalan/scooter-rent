from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_results, name='search_results'),
    path('scooter_list/', views.scooter_list, name='scooter_list'),
    path('pick_scooter/', views.pick_scooter, name='pick_scooter'),
    path('book_scooter/', views.book_scooter, name='book_scooter'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
