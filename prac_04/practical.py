"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    report(incomes)


def report(incomes):
    """Display the income report using the incomes list."""
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()

#2
def input_numbers():
    numbers = []
    count = 1
    while True:
        num = float(input(f"Number {count}: "))
        if num < 0:
            break
        numbers.append(num)
        count += 1
    return numbers

#3.
# lists_warmup.py

numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. What values do the following expressions have?
# numbers[0]            -> 3
# numbers[-1]           -> 2
# numbers[3]            -> 1
# numbers[:-1]          -> [3, 1, 4, 1, 5, 9]
# numbers[3:4]          -> [1]
# 5 in numbers          -> True
# 7 in numbers          -> False
# "3" in numbers        -> False
# numbers + [6, 5, 3]   -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# Print whether 9 is an element of numbers
print(9 in numbers)
# list_exercises.py
def input_numbers():
    numbers = []
    count = 1
    while True:
        try:
            num = float(input(f"Number {count}: "))
            if num < 0:
                break
            numbers.append(num)
            count += 1
        except ValueError:
            print("Please enter a valid number.")

    return numbers

if __name__ == "__main__":
    entered_numbers = input_numbers()
    print("Entered numbers:", entered_numbers)

#4.
def add_memberwise(list1, list2):
    min_length = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(min_length)] + list1[min_length:] + list2[min_length:]

print(add_memberwise([1, 2, 3], [4, 5, 6]))
print(add_memberwise([1, 2, 3], [1, 2, 3, 4]))