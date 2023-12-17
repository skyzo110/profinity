from .models import User, Employee, Document , Department, Project, Task, Milestone
from rest_framework import generics
from .serializers import UserSerializer, DocumentSerializer, DepartmentSerializer, ProjectSerializer, TaskSerializer, MilestoneSerializer, EmployeeSerializer
from django.contrib.auth.hashers import make_password


class UserCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DocumentCreateListView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DepartmentCreateListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectCreateListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskCreateListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class MilestoneCreateListView(generics.ListCreateAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class MilestoneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class EmployeeCreateListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class BlacklistTokenUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeRegistrationView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def perform_create(self, serializer):
        
        serializer.validated_data.pop('groups', None)
        serializer.validated_data.pop('user_permissions', None)
        
        password = serializer.validated_data.get('password')
        encoded_password = make_password(password)
        serializer.validated_data['password'] = encoded_password

        user = serializer.save()