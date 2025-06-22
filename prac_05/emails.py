"""
Email and Name Storage
Estimate: 25 minutes
Actual:   20 minutes
"""


def extract_name(email):
    """Extracts the name from the email by splitting on '.' and capitalizing."""
    base = email.split('@')[0]  # Get the part before the '@'
    name_parts = base.split('.')  # Split by '.'
    # Capitalize each part and join with a space
    return ' '.join(part.title() for part in name_parts)

def main():
    email_dict = {}
    while True:
        # Prompt user for email input
        email = input("Email: ").strip()
        if not email:  # If the input is blank, exit the loop
            break
        # Extract default name from email
        default_name = extract_name(email)
        name_confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if name_confirmation not in ['n', 'no']:
            # Use the default name if the confirmation is positive or blank
            name = default_name
        else:
            # Get the correct name from the user
            name = input("Name: ").strip()
        # Store the email and name in the dictionary
        email_dict[email] = name
    # Print the stored emails and names
    for email, name in email_dict.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()