from prac_09.taxi import Taxi

def main():
  # Create a new taxi object
  my_taxi = Taxi("Prius 1", 100, 1.23)

#Drive 40 kilometers.
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

#Reset the meter and drive 100 kilometers.
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"New fare after 100km: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
