from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancy Taxi with a higher fare and a flagfall charge."""
    
    flagfall = 4.50  # Class-level constant flagfall charge

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # override instance price

    def __str__(self):
        """Return a string representation, including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
