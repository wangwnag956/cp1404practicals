import datetime
from project import Project

DATE_FORMAT = "%d/%m/%Y"
DEFAULT_FILE = "projects.txt"

def load_projects(filename):
    projects = []
    with open(filename, encoding="utf-8") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) != 5:
                continue
            name, start_date_str, priority, cost_estimate, completion_percentage = parts
            start_date = datetime.datetime.strptime(start_date_str, DATE_FORMAT).date()
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w', encoding="utf-8") as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            print(str(project), file=file)


def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]
    print("Incomplete projects: ")
    for project in sorted(incomplete):
        print(f"  {project.display_string()}")
    print("Completed projects: ")
    for project in sorted(completed):
        print(f"  {project.display_string()}")

def filter_projects_by_date(projects, date_str):
    filter_date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
    filtered = [p for p in projects if p.start_date > filter_date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project.display_string())
