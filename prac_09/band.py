class Band:
    """A band with a name and a list of musicians."""

 def __init__(self, name):
    self.name = name
    self.musicians = []

 def __str__(self):
    return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})" 

 def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Tell each musician in the band to play."""
        for musician in self.musicians:
            musician.play()
