from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('todoList', views.todoList, name='todoList'),
    path('task_update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('change_password', views.change_password, name='change_password')
]