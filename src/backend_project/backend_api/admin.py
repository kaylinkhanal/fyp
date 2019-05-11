from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import (
                     User,
                     Student,
                     Faculty,
                     Subject,
                     SelectedSubject,
                     AttendanceRecord,
                     StudentOfTheYear,
                     Notice,
                     FacultyOfTheYear,
                     Choice,
                     Question,
                     Assignment,
                     GradedAssignment
)



class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_fields = ('email', 'username')
    ordering = ('email',)


admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SelectedSubject)
admin.site.register(Notice)
admin.site.register(StudentOfTheYear)
admin.site.register(FacultyOfTheYear)
admin.site.register(AttendanceRecord)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(GradedAssignment)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
