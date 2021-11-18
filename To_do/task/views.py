from django.shortcuts import render, HttpResponse, redirect
from task.models import Task
from task.forms import TaskForm

def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    print(tasks)
    context = {
        'task_list': tasks
    }
    # return HttpResponse("Hello {}".format(tasks[0]))
    return render(request, "task/home.html", context=context)

def task_delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect("home")
    task.delete()
    return redirect("home")


def task_create(request):
    create_form = TaskForm()

    if request.method == 'POST':
        print(request.POST)
        create_form = TaskForm(request.POST)
        if create_form.is_valid():
            # Task.objects.create(**create_form.cleaned_data)
            print(create_form.cleaned_data)
            name = create_form.cleaned_data['name']
            description = create_form.cleaned_data['description']
            status = create_form.cleaned_data['status']
            Task.objects.create(name=name, description=description, status=status)

            return redirect('home')

    context = {
        'form': create_form
    }
    return render(request, 'task/new_task.html', context=context)


def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')

    context = {'task': task, 'task_id': task.id}
    return render(request, "task/task_view.html", context=context)


def create_task(request):
    if request.method == "GET":

        return render(request, "task/index.html")
    else:
        name = request.POST.get('name')
        # status = request.POST.get('status')
        description = request.POST.get('description')
        print(name, description)
        Task.objects.create(name=name, description=description)
        print(Task.objects.all())
        return render(request, "task/index.html")

def task_update(request, task_id):
    return render(request, "task/task_update.html")