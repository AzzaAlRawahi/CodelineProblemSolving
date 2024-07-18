def display_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('1' * i)

def display_palindromic_triangle(n):
    for i in range(1, n + 1):
        left = ''.join(str(x) for x in range(1, i + 1))
        right = left[-2::-1]
        print(left + right)

def show_help():
    print("Help:")
    print("A Palindromic Triangle is a triangular array of numbers where each row forms a palindrome.")
    print("The first few lines of a Palindromic Triangle are:")
    print("1")
    print("11")
    print("121")
    print("12321")
    print("1234321")
    print("You can use this pattern to draw a Palindromic Triangle for any number of lines.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            n = int(input("Enter the number of lines: "))
            display_right_angle_triangle(n)
        elif choice == '2':
            n = int(input("Enter the number of lines: "))
            display_palindromic_triangle(n)
        elif choice == '3':
            show_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
