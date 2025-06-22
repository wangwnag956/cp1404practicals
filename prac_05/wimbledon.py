"""
Wimbledon Champions Data Processing
Estimate: 30 minutes
Actual:   25 minutes
"""

import csv
from collections import defaultdict

def read_wimbledon_data(filename):
    """Read Wimbledon champions data from CSV file."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header
        for row in reader:
            champions.append((row[0].strip(), row[1].strip()))  # (Champion, Country)
    return champions

def count_champions(champions):
    """Count the number of wins for each champion."""
    champion_count = defaultdict(int)
    for champion, _ in champions:
        champion_count[champion] += 1
    return champion_count

def get_unique_countries(champions):
    """Get a sorted list of unique countries."""
    countries = {country for _, country in champions}
    return sorted(countries)

def main():
    # Read data from the CSV file
    champions = read_wimbledon_data('wimbledon.csv')
    # Count the number of wins for each champion
    champion_count = count_champions(champions)
    # Get the unique countries
    unique_countries = get_unique_countries(champions)
    # Print the champions and their win counts
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")
    # Print the sorted unique countries
    print("\nThese {} countries have won Wimbledon:".format(len(unique_countries)))
    print(", ".join(unique_countries))

if __name__ == "__main__":
    main()