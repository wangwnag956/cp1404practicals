import datetime

DATE_FORMAT = "%d/%m/%Y"

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __lt__(self, other):
        """Sort by priority (asc), then start_date (asc)."""
        if self.priority == other.priority:
            return self.start_date < other.start_date
        return self.priority < other.priority

    def is_complete(self):
        """Check if the project is complete (100%)."""
        return self.completion_percentage == 100
