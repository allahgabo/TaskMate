from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm 
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request,'main/index.html')


@login_required
def todolist(request):
	if request.method =='POST':
		form=TaskForm(request.POST or None)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.manger=request.user 
			instance.save()
		messages.success(request,('New Taske Added'))
		return redirect('todolist')
	else:	
		tasks=TaskList.objects.filter(manger=request.user)
		paginator=Paginator(tasks,5)
		page=request.GET.get('page')
		tasks=paginator.get_page(page)
	return render(request,'main/todolist.html',{'tasks':tasks})

@login_required
def edit_task(request,task_id):
	if request.method =='POST':
		task=TaskList.objects.get(pk=task_id)
		form=TaskForm(request.POST or None , instance=task)
		if form.is_valid():
			form.save()
		messages.success(request,('Edited Task'))
		return redirect('todolist')
	else:	
		task_obj=TaskList.objects.get(pk=task_id)
	return render(request,'main/edit.html',{'task_obj':task_obj})


@login_required
def delete_task(request,task_id):
	task=TaskList.objects.get(pk=task_id)
	if task.manger == request.user:
		task.delete()
	else:
		messages.error(request,('Cant delete it '))
	return redirect('todolist')

@login_required
def complete_task(request,task_id):
	task=TaskList.objects.get(pk=task_id)
	if task.manger == request.user:
		task.done=True
		task.save()
	else:
		messages.error(request,('Access Dined'))

	return redirect('todolist')

@login_required
def pending_task(request,task_id):
	task=TaskList.objects.get(pk=task_id)
	task.done=False
	task.save()
	
	return redirect('todolist')


def about(request):
	return render(request,'main/about.html')



def contact(request):
	return render(request,'main/contact.html')
 