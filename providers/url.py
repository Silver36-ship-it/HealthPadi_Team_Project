from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_facilities, name='facility-list'),
    path('create/', views.create_facility, name='facility-create'),
    path('<int:pk>/', views.get_facility_detail, name='facility-detail'),
    path('<int:pk>/update/', views.update_facility, name='facility-update'),
    path('<int:pk>/delete/', views.delete_facility, name='facility-delete'),
]