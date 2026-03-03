# 📋 Task Manager

A web-based task management system built with Django, designed for teams.  
Managers can create and assign tasks; employees can take and complete them.

---

## 📸 Screenshots

### Login Page
<!-- screenshot: login page -->
> _Add screenshot here_

### Manager Dashboard – Task List
<!-- screenshot: task list with all statuses -->
> _Add screenshot here_

### Create New Task
<!-- screenshot: create task form -->
> _Add screenshot here_

### Employee View – Take a Task
<!-- screenshot: employee dashboard with Take Task button -->
> _Add screenshot here_

### Profile Page
<!-- screenshot: profile page -->
> _Add screenshot here_

---

## ✨ Features

- 🔐 **Authentication** – Register, login, and logout
- 👥 **Two roles** – Manager and Employee
- 📋 **Task management** – Create, edit, delete, and assign tasks
- ✅ **Task lifecycle** – New → In Progress → Completed
- 🔍 **Filtering** – Filter tasks by status, assignment, and worker
- 👤 **Profile page** – View and update personal info
- 🏢 **Team-based** – Each user belongs to a team and only sees their team's tasks

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · Django 6.0 |
| Frontend | HTML · CSS · Bootstrap 5 |
| Database | SQLite |
| Auth | Django Custom User |
| Forms | django-widget-tweaks |
| Environment | python-dotenv |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply migrations**
```bash
python manage.py migrate
```

**5. Load sample data** _(optional – for demo/screenshots)_
```bash
python seed_data.py
```

**6. Run the development server**
```bash
python manage.py runserver
```

Open your browser at: **http://127.0.0.1:8000**

---

## 👤 Demo Accounts

After running `seed_data.py`:

| Role | Username | Password | Team |
|------|----------|----------|------|
| Manager | `yaeli_porat` | `password123` | Alpha |
| Manager | `tamar_winer` | `password123` | Beta |
| Employee | `devora` | `password123` | Alpha |
| Employee | `shira` | `password123` | Alpha |
| Employee | `gili` | `password123` | Alpha |
| Employee | `pnini` | `password123` | Beta |
| Employee | `noa` | `password123` | Beta |

---

## 📁 Project Structure

```
task-manager/
├── task_manager/         # Project settings and URLs
│   ├── settings.py
│   └── urls.py
├── tasks/                # Main app
│   ├── models.py         # CustomUser, Team, Task
│   ├── views.py          # All views
│   ├── forms.py          # Task and user forms
│   ├── urls.py           # App routes
│   ├── admin.py
│   └── templates/
│       ├── accounts/     # Login, Register
│       └── tasks/        # Task list, create, update, delete, profile
├── static/
│   └── css/project.css
├── seed_data.py          # Demo data loader
├── manage.py
└── requirements.txt
```

---

## 🔄 How It Works

### Manager Flow
1. Log in as a manager
2. View all tasks in your team
3. Create a new task (optionally assign to an employee)
4. Edit or delete unassigned tasks

### Employee Flow
1. Log in as an employee
2. View all tasks in your team
3. Click **"Take Task"** to claim an unassigned task
4. Click **"Complete"** when done

---

## 📦 Dependencies

```
Django==6.0.2
django-widget-tweaks==1.5.1
python-dotenv==1.2.2
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2025.3
```

---

## 📄 License

This project is for educational purposes.
