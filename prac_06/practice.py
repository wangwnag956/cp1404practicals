

from car import car

def display_menu():
    print("Menu:\nd) drive\nr) refuel\nq) quit")

def get_menu_choice():
    choice = input("Enter your choice: ").lower()
    return choice

def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    car = car(car_name)

    print(car)
    display_menu()
    choice = get_menu_choice()

    while choice != 'q':
        if choice == 'd':
            drive_distance = get_valid_number("How many km do you wish to drive? ")
            print(car.drive(drive_distance))
        elif choice == 'r':
            refuel_amount = get_valid_number("How many units of fuel do you want to add to the car? ")
            print(car.refuel(refuel_amount))
        else:
            print("Invalid choice")

        print()
        print(car)
        display_menu()
        choice = get_menu_choice()

    print(f"\nGood bye {car.name}'s driver.")

def get_valid_number(prompt):
    number = int(input(prompt))
    while number < 0:
        print(f"{prompt.split('?')[0]} must be >= 0")
        number = int(input(prompt))
    return number

if __name__ == '__main__':
    main()
