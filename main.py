# fruits.py

# List of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Function to display all fruits
def display_fruits():
    print("Current list of fruits:")
    for fruit in fruits:
        print(f"- {fruit}")
    print()

# Function to add a fruit
def add_fruit(new_fruit):
    if new_fruit not in fruits:
        fruits.append(new_fruit)
        print(f"Added {new_fruit} to the list.")
    else:
        print(f"{new_fruit} is already in the list.")
    display_fruits()

# Function to remove a fruit
def remove_fruit(fruit_to_remove):
    if fruit_to_remove in fruits:
        fruits.remove(fruit_to_remove)
        print(f"Removed {fruit_to_remove} from the list.")
    else:
        print(f"{fruit_to_remove} is not in the list.")
    display_fruits()

# Main program
if __name__ == "__main__":
    print("Welcome to the Fruit Manager!")
    display_fruits()

    # Add a fruit
    add_fruit("fig")

    # Remove a fruit
    remove_fruit("banana")

    # Try adding a duplicate fruit
    add_fruit("apple")

    # Try removing a non-existent fruit
    remove_fruit("grape")