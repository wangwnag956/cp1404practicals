from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
  # Create a fancy Hummer with a degree of 4 (expected unit price = 1.23 * 4 = 4.92)
  fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
  fancy_taxi.start_fare()
  fancy_taxi.drive(18)
  print(fancy_taxi)
  # Obtain ticket prices and print them
  fare = fancy_taxi.get_fare()
    print(f"Fare for 18km = ${fare:.2f}")

# Use assert for verification (expected: 18 * 4.92 + 4.50 = 88.06)
    expected_fare = 18 * 4.92 + 4.50
    assert abs(fare - expected_fare) < 0.01, "Fare calculation error!" 

#retest
    fancy_taxi.start_fare()
    fancy_taxi.drive(2)
    fare = fancy_taxi.get_fare()
    print(f"Fare for 2km = ${fare:.2f}")

expected_fare = 2 * 4.92 + 4.50
    assert abs(fare - expected_fare) < 0.01, "Fare calculation error!"

if __name__ == "__main__":
    main()
