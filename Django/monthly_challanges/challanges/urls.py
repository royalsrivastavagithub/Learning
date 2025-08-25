from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>/', views.monthly_challange_by_number),
    path('<str:month>/', views.monthly_challange, name='month-challange'),
    path("", views.index , name="index"),
]
