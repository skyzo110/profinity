"""profinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Users/',views.UserCreateListView.as_view(), name='user-list'),
    path('Users/<int:pk>/',views.UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('Employees/',views.EmployeeCreateListView.as_view(), name='employee-list'),
    path('Employees/<int:pk>/',views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('Documents/',views.DocumentCreateListView.as_view(), name='document-list'),
    path('Documents/<int:pk>/',views.DocumentRetrieveUpdateDestroyView.as_view(), name='document-detail'),
    path('Departments/',views.DepartmentCreateListView.as_view(), name='department-list'),
    path('Departments/<int:pk>/',views.DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
    path('Projects/',views.ProjectCreateListView.as_view(), name='project-list'),
    path('Projects/<int:pk>/',views.ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('Tasks/',views.TaskCreateListView.as_view(), name='task-list'),
    path('Tasks/<int:pk>/',views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('Milestones/',views.MilestoneCreateListView.as_view(), name='milestone-list'),
    path('Milestones/<int:pk>/',views.MilestoneRetrieveUpdateDestroyView.as_view(), name='milestone-detail'),
    path('Employees/',views.EmployeeCreateListView.as_view(), name='employee-list'),
    path('Employees/<int:pk>/',views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/blacklist/', views.BlacklistTokenUpdateView.as_view(), name='blacklist'),

]
