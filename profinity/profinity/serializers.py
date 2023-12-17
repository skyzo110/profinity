import pdb
from rest_framework import serializers
from .models import  User, Document, Department, Project, Task, Milestone, Employee
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document 
        fields = '__all__'


    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)

            token['id'] = user.id
            token['email'] = user.email
            token['username'] = user.username
            token['is_active'] = user.is_active
            token['is_admin'] = user.is_admin
            token['is_superuser'] = user.is_superuser

            return token 
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            resume=validated_data['resume'],
            image=validated_data['image'],
            date_of_birth=validated_data['date_of_birth'],
            department=validated_data['department'],
            position=validated_data['position'],
            experience=validated_data['experience'],
            salary=validated_data['salary'],
            propoints=validated_data['propoints'],
            Employment_Status=validated_data['Employment_Status'],
            Work_Schedule=validated_data['Work_Schedule'],
            Skills_and_Qualifications=validated_data['Skills_and_Qualifications'],
            Performance_Ratings=validated_data['Performance_Ratings'],
            ROI=validated_data['ROI'],
            milestones_passed=validated_data['milestones_passed'],
            assigned_tasks=validated_data['assigned_tasks'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class documentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        document = Document(
            name=validated_data['name'],
            description=validated_data['description'],
            file=validated_data['file'],
        )
        document.save()
        return document
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        department = Department(
            name=validated_data['name'],
            description=validated_data['description'],
        )
        department.save()
        return department
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        project = Project(
            name=validated_data['name'],
            description=validated_data['description'],
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            status=validated_data['status'],
            department=validated_data['department'],
            milestones=validated_data['milestones'],
            employees=validated_data['employees'],
            documents=validated_data['documents'],
            tasks=validated_data['tasks'],
        )
        project.save()
        return project
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        task = Task(
            name=validated_data['name'],
            description=validated_data['description'],
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            status=validated_data['status'],
            project=validated_data['project'],
            employees=validated_data['employees'],
            documents=validated_data['documents'],
        )
        task.save()
        return task
    
class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        milestone = Milestone(
            name=validated_data['name'],
            description=validated_data['description'],
        )
        milestone.save()
        return milestone
    

