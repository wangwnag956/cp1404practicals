from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def run_simulator(taxis, current_taxi=None, total_bill=0.0):
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()

    if choice == 'q':
        # End recursion, exit program
        print(f"Total trip cost: ${total_bill:.2f}")
        print("Taxis are now:")
        display_taxis(taxis)
        return  
