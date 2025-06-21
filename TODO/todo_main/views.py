
from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task


def home(request):
    # return HttpResponse('<h2>Homepage</h2>')
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    # print(tasks)
    context={
        'tasks':tasks,
    }
    return render(request,'home.html',context)

# def add_task(request):
#     if request.method == "POST":
#         task_text = request.POST.get("task")
#         if task_text:
#             # Save to your model (e.g., Task.objects.create(task=task_text))
#             Task.objects.create(task=task_text)
#     return redirect('home')