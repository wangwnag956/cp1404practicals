class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year=2022):
        """Return the actual age of the guitar."""
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than comparison for sorting by year (older first)."""
        return self.year < other.year
