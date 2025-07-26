import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car that might not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability
