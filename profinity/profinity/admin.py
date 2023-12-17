from django.contrib import admin
from .models import User, Employee, Document, Department, Project, Task, Milestone


admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Milestone)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass