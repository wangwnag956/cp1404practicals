"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subjects(data)

def load_data():
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subjects(data):
    for record in data:
        subject, lecturer, student_count = record
        print(f"{subject} is taught by {lecturer} and has {student_count} students")

if __name__ == '__main__':
    main()