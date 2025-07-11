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

def add_project():
    #Responsible for obtaining user input.
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    try:
        start_date = datetime.datetime.strptime(date_str, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format. Project not added.")
        return None

    try:
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
    except ValueError:
        print("Invalid numeric input. Project not added.")
        return None

    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project.display_string()}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project.display_string())
        percent_str = input("New Percentage: ")
        if percent_str:
            project.completion_percentage = int(percent_str)
        priority_str = input("New Priority: ")
        if priority_str:
            project.priority = int(priority_str)
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")

    MENU = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    choice = input_menu_choice(MENU)
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")

        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_str)
        elif choice == "a":
            project = add_project()
            if project:
                projects.append(project)
        elif choice == "u":
            update_project(projects)

        choice = input_menu_choice(MENU)


    save = input(f"Would you like to save to {DEFAULT_FILE}? (y/n): ").strip().lower()
    if save == 'y':
        save_projects(DEFAULT_FILE, projects)
        print(f"Saved projects to {DEFAULT_FILE}.")
    print("Thank you for using custom-built project management software.")


def input_menu_choice(menu):
    print(menu)
    return input(">>> ").strip().lower()
