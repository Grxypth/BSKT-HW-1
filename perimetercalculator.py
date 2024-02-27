def get_num(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def calculate_perimeter(length, width):
    return 2 * (length + width)

def main():
    
    while True:
        length = get_num("Enter the length of the rectangle: ")
        width = get_num("Enter the width of the rectangle: ")

        perimeter = calculate_perimeter(length, width)
        print("The perimeter of the rectangle is:", perimeter)

        try:
            choice = input("Calculate the perimeter of another rectangle? (y/n): ").strip().lower()
            if choice != 'y':
                print("Exiting the program.")
                break
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()