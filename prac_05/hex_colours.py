"""
Hex Color Lookup
Estimate: 20minutes
Actual:   18 minutes
"""

# Dictionary of color names and their corresponding hexadecimal codes
COLOR_CODES = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "Alice Blue": "#f0f8ff",
    "Amaranth Red": "#e32636",
    "Eggplant": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "Antique White": "#faebd7",
    "Aquamarine 1": "#7fffd4",
    "Army Green": "#4b5320",
}


def color_lookup():
    while True:
        # Get user input for the color name
        color_name = input("Enter a color name (or press Enter to exit): ").strip()

        if not color_name:  # Exit if input is empty
            break

        # Process input case-insensitively
        color_name_lower = color_name.lower()
        for name, hex_code in COLOR_CODES.items():
            if name.lower() == color_name_lower:
                print(f"{name} ({color_name_lower}) has the hexadecimal code: {hex_code}")
                break
        else:
            print("Invalid color name, please try again.")


# Run the program
color_lookup()