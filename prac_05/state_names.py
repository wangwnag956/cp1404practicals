"""
CP1404/CP5632 Practical
State names in a dictionary
"""
# Use the dictionary formatted according to PEP 8 standards
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

#Print the names and abbreviations of all states.
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

# Get user input and process it
while True:
    state_code = input("Enter short state (or press Enter to quit): ").strip()
    if not state_code: # Check if the user has entered an empty string
        break
    try:
        # Convert the short status codes to uppercase to support lowercase input
        state_code_upper = state_code.upper()
        # Access the dictionary to find the full name
        print(f"{state_code_upper} is {CODE_TO_NAME[state_code_upper]}")
    except KeyError:  # If not found in the dictionary, raise an exception
        print("Invalid short state")