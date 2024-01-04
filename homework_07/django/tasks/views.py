from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
import datetime

# Create your views here.


def list(request):
    if not request.user.is_authenticated:
        return redirect("user:sign_in")

    finished_tasks = Task.objects.filter(
        user=request.user, is_completed=True, is_deleted=False
    )
    unfinished_tasks = Task.objects.filter(
        user=request.user, is_completed=False, is_deleted=False
    )
    context = {"finished_tasks": finished_tasks, "unfinished_tasks": unfinished_tasks}
    return render(request, "list.html", context)


def create(request):
    if request.method == "POST":
        try:
            title = request.POST["title"]
            description = request.POST["description"]

            date = request.POST["date"]
            time = request.POST["time"]

            year, month, day = [int(v) for v in date.split("-")]
            hh, mm = [int(v) for v in time.split(":")]

            close_date = datetime.datetime.combine(
                datetime.date(year, month, day), datetime.time(hh, mm)
            )

            task = Task.objects.create(
                title=title,
                description=description,
                close_date=close_date,
                user=request.user,
            )
            task.save()

            messages.success(request, "Task created")
            return redirect("tasks:list")
        except:
            messages.error(request, "Something went wrong")

    return render(request, "create.html")


def delete(request, task_id):
    try:
        task = Task.objects.get(user=request.user, id=task_id)
        if task:
            task.is_deleted = True
            task.save()
            messages.success(request, "Task deleted")
    except:
        messages.error(request, "Something went wrong")
    finally:
        return redirect("tasks:list")


def complete(request, task_id):
    try:
        task = Task.objects.get(user=request.user, id=task_id)
        if task:
            task.is_completed = True
            task.save()
            messages.success(request, "Task finished. Congrats!")

    except:
        messages.error(request, "Something went wrong")
    finally:
        return redirect("tasks:list")


def uncomplete(request, task_id):
    try:
        task = Task.objects.get(user=request.user, id=task_id)
        if task:
            task.is_completed = False
            task.save()
            messages.success(request, "Task uncompleted")

    except:
        messages.error(request, "Something went wrong")
    finally:
        return redirect("tasks:list")
