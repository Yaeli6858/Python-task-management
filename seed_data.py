"""
Seed script - מריץ מידע לדוגמה לפרויקט Task Manager
הרץ עם: python seed_data.py
"""

import os
import django
from datetime import date, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
django.setup()

from tasks.models import CustomUser, Team, Task
from django.contrib.auth.hashers import make_password

print("Cleaning old data...")
Task.objects.all().delete()
Team.objects.all().delete()
CustomUser.objects.all().delete()

print("Creating users...")

# Managers
manager1 = CustomUser.objects.create(
    username="yaeli_porat",
    first_name="Yaeli",
    last_name="Porat",
    email="yaeli@company.com",
    password=make_password("password123"),
    userStatus=0,
    phone="050-1234567",
    is_staff=True,
    is_superuser=True,
)

manager2 = CustomUser.objects.create(
    username="tamar_winer",
    first_name="Tamar",
    last_name="Winer",
    email="tamar@company.com",
    password=make_password("password123"),
    userStatus=0,
    phone="052-9876543",
)

# Employees
employees = []
emp_data = [
    ("devora", "Devora", "Cohen",     "054-1112233"),
    ("shira",  "Shira",  "Levi",      "053-4445566"),
    ("gili",   "Gili",   "Mizrahi",   "058-7778899"),
    ("pnini",  "Pnini",  "Ben-David", "050-3334455"),
    ("noa",    "Noa",    "Shapiro",   "052-6667788"),
]
for uname, first, last, phone in emp_data:
    emp = CustomUser.objects.create(
        username=uname,
        first_name=first,
        last_name=last,
        email=f"{uname}@company.com",
        password=make_password("password123"),
        userStatus=1,
        phone=phone,
    )
    employees.append(emp)

devora, shira, gili, pnini, noa = employees

print("Creating teams...")

team_alpha = Team.objects.create(name="Alpha", manager=manager1)
team_beta  = Team.objects.create(name="Beta",  manager=manager2)

for user in [manager1, devora, shira, gili]:
    user.team = team_alpha
    user.save()

for user in [manager2, pnini, noa]:
    user.team = team_beta
    user.save()

print("Creating tasks...")

today = date.today()

tasks_alpha = [
    {
        "title": "Design new landing page",
        "description": "Redesign the company homepage with modern UI/UX principles. Include hero section, testimonials, and CTA buttons.",
        "goalDate": today + timedelta(days=5),
        "taskStatus": 2,
        "task_performer": devora,
        "task_manager": manager1,
        "team": team_alpha,
    },
    {
        "title": "Fix login bug on mobile",
        "description": "Users on iOS 17 cannot log in via Safari. Reproduce and fix the issue. Update regression tests.",
        "goalDate": today + timedelta(days=2),
        "taskStatus": 1,
        "task_performer": shira,
        "task_manager": manager1,
        "team": team_alpha,
    },
    {
        "title": "Write API documentation",
        "description": "Document all REST endpoints using Swagger. Cover authentication, request/response schemas, and error codes.",
        "goalDate": today + timedelta(days=10),
        "taskStatus": 1,
        "task_performer": gili,
        "task_manager": manager1,
        "team": team_alpha,
    },
    {
        "title": "Set up CI/CD pipeline",
        "description": "Configure GitHub Actions to run tests and deploy to staging automatically on every pull request.",
        "goalDate": today + timedelta(days=7),
        "taskStatus": 0,
        "task_performer": None,
        "task_manager": manager1,
        "team": team_alpha,
    },
    {
        "title": "Migrate database to PostgreSQL",
        "description": "Replace the current SQLite setup with PostgreSQL for production. Write migration scripts and update settings.",
        "goalDate": today + timedelta(days=14),
        "taskStatus": 0,
        "task_performer": None,
        "task_manager": manager1,
        "team": team_alpha,
    },
    {
        "title": "Code review - payment module",
        "description": "Review PR #87 for the new Stripe integration. Check security, error handling, and test coverage.",
        "goalDate": today + timedelta(days=3),
        "taskStatus": 2,
        "task_performer": shira,
        "task_manager": manager1,
        "team": team_alpha,
    },
]

tasks_beta = [
    {
        "title": "Create monthly sales report",
        "description": "Compile Q1 sales data into an executive report. Include charts, KPIs, and quarter-over-quarter comparison.",
        "goalDate": today + timedelta(days=4),
        "taskStatus": 1,
        "task_performer": noa,
        "task_manager": manager2,
        "team": team_beta,
    },
    {
        "title": "Onboard new client - TechStart Ltd",
        "description": "Complete the onboarding checklist for TechStart Ltd: contract signed, accounts created, intro call scheduled.",
        "goalDate": today + timedelta(days=6),
        "taskStatus": 0,
        "task_performer": None,
        "task_manager": manager2,
        "team": team_beta,
    },
    {
        "title": "Update privacy policy",
        "description": "Review and update the privacy policy to comply with GDPR changes effective next month. Coordinate with legal.",
        "goalDate": today + timedelta(days=9),
        "taskStatus": 1,
        "task_performer": pnini,
        "task_manager": manager2,
        "team": team_beta,
    },
    {
        "title": "Prepare investor pitch deck",
        "description": "Build a 15-slide pitch deck for the Series A round. Include product demo, market size, traction, and financials.",
        "goalDate": today + timedelta(days=12),
        "taskStatus": 0,
        "task_performer": None,
        "task_manager": manager2,
        "team": team_beta,
    },
    {
        "title": "Customer satisfaction survey",
        "description": "Design and send NPS survey to all active customers. Analyze results and present findings to the team.",
        "goalDate": today + timedelta(days=8),
        "taskStatus": 2,
        "task_performer": noa,
        "task_manager": manager2,
        "team": team_beta,
    },
]

for t in tasks_alpha + tasks_beta:
    Task.objects.create(**t)

print("\n=================================================")
print("  Seed complete!")
print("=================================================")
print("MANAGER ACCOUNTS:")
print("  username: yaeli_porat  | password: password123  (Team Alpha)")
print("  username: tamar_winer  | password: password123  (Team Beta)")
print()
print("EMPLOYEE ACCOUNTS:")
print("  username: devora  | password: password123  (Alpha)")
print("  username: shira   | password: password123  (Alpha)")
print("  username: gili    | password: password123  (Alpha)")
print("  username: pnini   | password: password123  (Beta)")
print("  username: noa     | password: password123  (Beta)")
print()
print(f"Created: {Task.objects.count()} tasks, {Team.objects.count()} teams, {CustomUser.objects.count()} users")
print("=================================================")
