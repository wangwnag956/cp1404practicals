import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car that might not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

  def drive(self, distance):
        """
        Drive the car only if a random number is less than the car's reliability.
        Return the actual distance driven.
        """
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0  # The car did not drive
