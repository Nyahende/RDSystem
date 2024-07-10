from django.urls import path
from . import views

urlpatterns = [
    path('permits/', views.permit_list, name='permit_list'),
    path('permits/<int:permit_id>/', views.permit_detail, name='permit_detail'),
    path('permits/<int:permit_id>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('charts/', views.chart_data, name='chart_data'),
    
    path('permits/create/', views.create_permit, name='create_permit'),
    path('permits/<int:permit_id>/update/', views.update_permit, name='update_permit'),
    path('permits/<int:permit_id>/delete/', views.delete_permit, name='delete_permit'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),


]
