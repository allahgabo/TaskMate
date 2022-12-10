from django.urls import path
from . import views

urlpatterns=[
	path("",views.index,name='index'),
	path('todolist',views.todolist,name='todolist'),
	path('delete/<task_id>/',views.delete_task,name='delete-task'),
	path('edit/<task_id>/',views.edit_task,name='edit-task'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('complete/<task_id>/',views.complete_task,name='complete-task'),
	path('pending/<task_id>/',views.pending_task,name='pending-task'),
]