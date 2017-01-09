from django.contrib import admin
from .models import Question
from .models import Choice
from .models import ToDo
from .models import UserProfile


class ToDoAdmin(admin.ModelAdmin):

    model = ToDo
    list_display = ('todo', 'pub_date', 'user', 'work')
    ordering = ('pub_date', 'work')


class UserProfileAdmin(admin.ModelAdmin):

    model = UserProfile
    list_display = ('user', 'name', 'last_name', 'age')
    ordering = ('age', 'name')

admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ToDo, ToDoAdmin)


