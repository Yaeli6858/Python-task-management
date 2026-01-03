from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import TaskForm, CustomUserCreationForm, TaskFilterForm,ProfileForm
from .models import Task


@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user

        if not user.team:
            return Task.objects.none()

        qs = Task.objects.filter(team=user.team)

        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(taskStatus=int(status))

        worker_id = self.request.GET.get('worker_id')
        assigned_filter = self.request.GET.get('assigned')

        if worker_id:
            qs = qs.filter(task_performer__id=worker_id)
        elif assigned_filter == 'assigned':
            qs = qs.filter(task_performer__isnull=False)
        elif assigned_filter == 'unassigned':
            qs = qs.filter(task_performer__isnull=True)

        return qs.order_by('goalDate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskFilterForm(self.request.user, self.request.GET)
        return context


@method_decorator(login_required, name='dispatch')
class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.userStatus != 0:  # רק מנהל
            return redirect('task_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.task_manager = self.request.user
        task.team = self.request.user.team

        if task.task_performer:
            task.taskStatus = 1
        else:
            task.taskStatus = 0

        task.save()
        return redirect('task_list')


@method_decorator(login_required, name='dispatch')
class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_task.html'
    context_object_name = 'task'
    success_url = '/tasks/'

    def get_queryset(self):
        user = self.request.user
        if user.userStatus == 0:  # מנהל
            return Task.objects.filter(team=user.team, task_performer__isnull=True)
        else:  # עובד
            return Task.objects.filter(task_performer=user)

    # כאן מוסיפים את form_valid כדי לעדכן את סטטוס
    def form_valid(self, form):
        task = form.save(commit=False)

        # אם יש task_performer, סטטוס צריך להיות In Progress
        if task.task_performer:
            task.taskStatus = 1  # In Progress
        else:
            task.taskStatus = 0  # New

        task.save()
        return redirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    context_object_name = 'task'
    success_url = '/tasks/'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(
            team=user.team,
            task_performer__isnull=True,
            task_manager=user
        )


@login_required
def take_task_view(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        task_performer__isnull=True,
        team=request.user.team
    )

    if request.user.userStatus == 1:  # עובד
        task.task_performer = request.user
        task.taskStatus = 1
        task.save()

    return redirect('task_list')


@login_required
def profile_view(request):
    return render(request, "tasks/profile.html", {
        "user": request.user
    })


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("task_list")
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
from .forms import ProfileForm

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'tasks/profile.html', {'form': form})

@login_required
def complete_task_view(request, pk):
    task = get_object_or_404(
        Task,
        pk=pk,
        task_performer=request.user,  # רק עובד שהשלים משימה יכול לסמן
        team=request.user.team
    )

    if request.method == "POST":
        task.taskStatus = 2  # Completed
        task.save()

    return redirect('task_list')
