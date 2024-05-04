

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.risk_assessment_page, name='risk_assessment_page'),
    path('add/', views.add_assessment, name='add_assessment'),
    path('get_user_assessments/<int:risk_assessment_id>/', views.get_user_assessments, name='get_user_assessments'),
    path('get_user_assessment_assement_id/<int:user_assessment_id>/', views.get_user_assessment_assement_id, name='get_user_assessment_assement_id'),
    path('delete_user_assessment/', views.delete_user_assessment, name='delete_user_assessment'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('import-from-excel/', views.import_from_excel, name='import_from_excel'),
    path('change_status/<int:assessment_id>/', views.change_status, name='change_status'),
    path('add_user_control/', views.add_user_control, name='add_user_control'),
]
