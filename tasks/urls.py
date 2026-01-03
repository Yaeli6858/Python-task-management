from django.urls import path
from . import views

urlpatterns = [

path("", views.TaskListView.as_view(), name="home"),
    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # Tasks
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("tasks/create/", views.CreateTaskView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", views.UpdateTaskView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", views.DeleteTaskView.as_view(), name="task_delete"),

path('tasks/<int:pk>/take/', views.take_task_view, name='task_take'),
path("profile/", views.profile_view, name="profile")
]

