from django.contrib import admin
from .models import TaskList

class TaskAdmin(admin.ModelAdmin):
	list_display=['task','done']


admin.site.register(TaskList,TaskAdmin)
