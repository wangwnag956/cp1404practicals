"""
CP1404
"""
def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total_income = 0
    for month_number, income in enumerate(incomes, start=1):
        total_income += income
        print(f"Month {month_number:2} - Income: ${income:10.2f} Total: ${total_income:10.2f}")


def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)

if __name__ == '__main__':
    main()