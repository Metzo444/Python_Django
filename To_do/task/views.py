from django.shortcuts import render, HttpResponse, redirect

from task.forms import TaskForm, TaskUpdateForm, TaskModelForm
from task.models import Task


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


def task_update(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')

    form = TaskUpdateForm(instance=task)

    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'task': task,
        'form': form
    }

    return render(request, "task/task_update.html", context=context)


# def task_update(request, task_id):
#     try:
#         task = Task.objects.get(id=task_id)
#     except Task.DoesNotExist:
#         return redirect("home")
#
#
#     data = dict(description=task.description, status = task.status)
#
#     form = TaskUpdateForm(data)
#
#     if request.method  == 'POST':
#         form = TaskUpdateForm(request.POST)
#         if form.is_valid():
#             task.status = form.cleaned_data['status']
#             task.description = form.cleaned_data['description']
#             task.save()
#             return redirect('home')
#     context = {
#         'task': task,
#         'form': form
#     }
#
#     return render(request, 'task/task_update.html', context=context)


def task_create(request):
    create_form = TaskModelForm()

    if request.method == 'POST':
        create_form = TaskModelForm(request.POST)
        if create_form.is_valid():
            # Task.objects.create(**create_form.cleaned_data)
            # print(create_form.cleaned_data)
            # name = create_form.cleaned_data['name']
            # description = create_form.cleaned_data['description']
            # status = create_form.cleaned_data['status']
            # Task.objects.create(name=name, description=description, status=status)
            create_form.save()
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
