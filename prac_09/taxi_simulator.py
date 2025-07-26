from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    #Display the list of taxis along with their numbers
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def run_simulator(taxis, current_taxi=None, total_bill=0.0):
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()

    if choice == 'q':
        # The user chooses to exit. Print the total bill and all taxi information, and terminate the recursion.
        print(f"Total trip cost: ${total_bill:.2f}")
        print("Taxis are now:")
        display_taxis(taxis)
        return  


    elif choice == 'c':
        display_taxis(taxis)
        try:
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid taxi choice")

    elif choice == 'd':
        # User selects to take a taxi
        if current_taxi is None:
            print("You need to choose a taxi before you can drive")
            print(f"Bill to date: ${total_bill:.2f}")
        else:
            try:
                distance = float(input("Drive how far? "))
                if distance < 0:
                    print("Distance must be >= 0")
                else:
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    total_bill += fare
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    print(f"Bill to date: ${total_bill:.2f}")
            except ValueError:
                print("Invalid distance")

    else:
        # Handling of Illegal Options
        print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

# Make recursive calls to itself and pass the updated state
 run_simulator(taxis, current_taxi, total_bill)

def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    print("Let's drive!")
    run_simulator(taxis)

if __name__ == '__main__':
    main()
