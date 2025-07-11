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
