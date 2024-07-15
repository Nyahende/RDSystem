from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_views.create_monitoring, name='create_monitoring'),
    path('list/', views.monitoring_list, name='monitoring_list'),
    path('detail/<int:pk>/', views.monitoring_detail, name='monitoring_detail'),
    path('report_chart/', views.report_chart, name='report_chart'),
]
