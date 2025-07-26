from prac_09.unreliable_car import UnreliableCar

def main():
  # Create a car with a reliability of 50
  car = UnreliableCar("Old Rusty", 100, 50)

 total_attempts = 10
 print(f"Testing {car.name} with reliability {car.reliability}%")

 for attempt in range(1, total_attempts + 1):
    distance = 10
    actual_distance = car.drive(distance)
    print(f"Attempt {attempt}: Tried to drive {distance}km, actually drove {actual_distance}km")

  print(f"Final odometer: {car.odometer}km, Remaining fuel: {car.fuel}L")

  if __name__ == "__main__":
     main()
