from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from .forms import TaskForm
import datetime


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'list.html'
    login_url = reverse_lazy("user:sign_in")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'finished_tasks': context['object_list'][0],
            'unfinished_tasks': context['object_list'][1],
        })

        return context

    def get_queryset(self):
        finished_tasks = Task.objects.filter(
            user=self.request.user, is_completed=True, is_deleted=False
        )
        unfinished_tasks = Task.objects.filter(
            user=self.request.user, is_completed=False, is_deleted=False
        )

        return (finished_tasks,  unfinished_tasks)


class TasksDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Task
    login_url = reverse_lazy("user:sign_in")


class TasksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy("user:sign_in")
    template_name = 'create.html'
    success_url = reverse_lazy('tasks:list')
    success_message = 'Task created'

    def form_valid(self, form):
        date = form.cleaned_data["date"]
        time = form.cleaned_data["time"]

        close_date = datetime.datetime.combine(date, time)

        form.instance.close_date = close_date  # type: ignore
        form.instance.user = self.request.user  # type: ignore

        return super(TasksCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return super().form_invalid(form)


class TasksDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
    success_message = 'Task deleted'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TasksUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('tasks:list')

    def post(self, request, *args, **kwargs):
        try:
            id = kwargs['pk']
            action = request.GET.get('action', None)

            task = Task.objects.get(user=request.user, id=id)
            task.is_completed = True if action == 'complete' else False
            task.save()
            messages.success(request, "Task finished. Congrats!")
        except:
            messages.error(request, "Something went wrong")
        finally:
            return redirect("tasks:list")
