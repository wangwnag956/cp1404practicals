from guitar import Guitar

def load_guitars(filename):
    """Load guitars from a csv file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name, year, cost = parts
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    return guitars

def save_guitars(filename, guitars):
    """Save guitars to a csv file."""
    with open(filename, 'w', encoding='utf-8') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    """Display all guitars in the list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")
