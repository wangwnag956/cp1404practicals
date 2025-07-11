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
        
 def __str__(self):
        """File/tab-separated string for saving."""
        return (f"{self.name}\t"
                f"{self.start_date.strftime(DATE_FORMAT)}\t"
                f"{self.priority}\t"
                f"{self.cost_estimate}\t"
                f"{self.completion_percentage}")

    def display_string(self):
        """User-friendly string for display."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")
