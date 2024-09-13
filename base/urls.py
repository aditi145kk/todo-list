from django.urls import path
from .views import (
    TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView,
    TaskReorder, CustomLoginView, RegisterPage
)
from .views import custom_logout


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('reorder-tasks/', TaskReorder.as_view(), name='task-reorder'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', custom_logout, name='logout'),
]
