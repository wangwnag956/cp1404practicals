from guitar import Guitar

def main():
    print("My guitars!")
    guitars = get_guitars_from_user()

   if guitars: 
      print("\nThese are my guitars:")
      for i, guitar in enumerate(guitars, 1):
          vintage_string = " (vintage)" if guitar.is_vintage() else ""
          print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
                f"worth ${guitar.cost:10,.2f}{vintage_string}")

    else:
        print("No guitars entered.")
