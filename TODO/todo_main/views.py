
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    # return HttpResponse('<h2>Homepage</h2>')
    return render(request,'home.html')

def add_task(request):
    if request.method == "POST":
        task_text = request.POST.get("task")
        if task_text:
            # Save to your model (e.g., Task.objects.create(task=task_text))
            pass
    return redirect('home')