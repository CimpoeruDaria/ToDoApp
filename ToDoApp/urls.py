from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='ToDoApp/login.html'), name = "login"),
    path('main_page/', views.main_page_view, name = "main_page"), 
    path('create/', views.task_create_view, name = "task_create"), 
    path('delete/<int:task_id>/', views.task_delete_view, name = "task_delete"), 
    path('login/', auth_views.LoginView.as_view(template_name='ToDoApp/login.html'), name = "login"), 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"), 
    path('register/', views.register_view, name = "register"),
    path('toggle/<int:task_id>', views.task_toggle_complete_view, name = 'task_toggle'), 
    
]