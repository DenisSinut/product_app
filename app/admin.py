from django.contrib import admin
from app.models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    fields = ['first_name', 'last_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'start_time', 'show_lessons', 'price']
    fields = ['title', 'owner', 'start_time', 'price', 'lessons', 'max_count', 'min_count']
    def show_lessons(self, obj):
        return [a.title for a in obj.lessons.all()]

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['student', 'product', 'value']
    fields = ['student', 'product', 'value']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
    fields = ['title', 'link']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'show_students']
    fields = ['title', 'students', 'product']

    def show_students(self, obj):
        #return list(obj.students.all().values_list('first_name'))
        #return "\n".join([a.first_name for a in obj.students.all()])
        return [a.first_name for a in obj.students.all()]