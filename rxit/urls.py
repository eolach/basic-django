from django.urls import path
from rxit import views

urlpatterns = [
    path('prescribers/', views.prescriber_list),
    path('prescribers/<int:pk>/', views.prescriber_detail),
]