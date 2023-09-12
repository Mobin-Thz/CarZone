
from django.urls import path
from . import views
urlpatterns = [
    path('cars/', views.cars, name='cars'),
    path('car/<str:id>', views.car_detail, name = 'car_detail'),

]
