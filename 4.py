def calculate_fact(a):
    """Recursively calculates the factorial of a number."""
    if a < 1:
        return 1
    else:
        return a * calculate_fact(a - 1)

def taken_user_list_input():
    """Takes input from the user and stores it in a list."""
    user_input = input("Enter the data for 1D array (separated by spaces): ")
    # Use user_input to split and convert the input into a list of integers
    user_list = [int(num) for num in user_input.split()]
    
    print("Data has been stored successfully!")
    print("Your list:", *user_list)
    
    return user_list  # Return the list so we can use it later

def count_number_on_userlist(user_list):
    """Count the number of elements in the user list."""
    if user_list:  # Check if the list is not empty
       count = len(user_list)  # Use len() to get the count of items in the list
       print(f"- Total Elements: {count}")
    else:
        print("- The list is empty.")
        
def minimum_number_on_userlist(user_list):
    """Find the minimum number in the user list."""
    if user_list:  # Check if the list is not empty
        minimum = min(user_list)  # Use min() to get the smallest element in the list
        print(f"- Minimum Element: {minimum}")
    else:
        print("- The list is empty.")

def maximum_number_on_userlist(user_list):
    """Find the maximum number in the user list."""
    if user_list:  # Check if the list is not empty
        maximum = max(user_list)  # Use max() to get the largest element in the list
        print(f"- Maximum Element: {maximum}")
    else:
        print("- The list is empty.")

def sum_number_on_userlist(user_list):
    """Find the sum of the elements in the user list."""
    if user_list:  # Check if the list is not empty
        total_sum = sum(user_list)  # Use sum() to get the sum of the elements
        print(f"- Sum of Elements: {total_sum}")
    else:
        print("- The list is empty.")

def average_number_on_userlist(user_list):
    """Find the average of the elements in the user list."""
    if user_list:  # Check if the list is not empty
        average = sum(user_list) / len(user_list)  # Calculate the average
        print(f"- Average Value: {average}")
    else:
        print("- The list is empty.")

def number_in_ascending(user_list):
    """Sort the list in ascending order."""
    if user_list:
        sorted_list = sorted(user_list)  # Sort in ascending order
        print("\nSorted Data in Ascending Order:")
        print(*sorted_list)
    else:
        print("- The list is empty.")

def number_in_descending(user_list):
    """Sort the list in descending order."""
    if user_list:
        sorted_list = sorted(user_list, reverse=True)  # Sort in descending order
        print("\nSorted Data in Descending Order:")
        print(*sorted_list)
    else:
        print("- The list is empty.")

def Statistics_number(user_list):
    """Calculate the minimum, maximum, sum, and average of the list."""
    if not user_list:
        return None, None, None, None

    minimum = user_list[0]
    maximum = user_list[0]
    sum_list = 0

    for number in user_list:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
        sum_list += number

    average = sum_list / len(user_list)
    return minimum, maximum, sum_list, average

        
        
print("Welcome to the Data Analyzer and Transformer Program")

# Variable to store user data
user_list = []

while True:
    print("\n")
    print("Main menu:")
    print("1. Input Data")
    print("2. Display The Data Summary (built-in function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda function)")
    print("5. Sort Data")
    print("6. Display Data Statistics (Return multiple values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            user_list = taken_user_list_input()  # Now it works because the function is defined properly
        
        case "2":
            print("Data Summary:")
            if user_list:  # Check if the user list is not empty
                count_number_on_userlist(user_list)  # Pass the user_list to the counting function
                minimum_number_on_userlist(user_list)  # Pass the user_list to the minimum function
                maximum_number_on_userlist(user_list)  # Pass the user_list to the maximum function
                sum_number_on_userlist(user_list)  # Pass the user_list to the sum function
                average_number_on_userlist(user_list)  # Pass the user_list to the average function
            else:
                print("- No data available. Please input data first.")
        
        case "3":
           
                number = int(input("Enter a Number: "))
                f = calculate_fact(number)
                print(f"Factorial of {number} is: {f}")
            
        case "4":
            if user_list:  # Check if the list is not empty
                    threshold = int(input("Enter the threshold value: "))
                    # Use lambda and filter to get numbers greater than the threshold
                    filtered_list = list(filter(lambda x: x > threshold, user_list))
                    if filtered_list:
                        print("Values above the threshold:")
                        print(*filtered_list)
                    else:
                        print("No values exceed the threshold.")
               
            else:
                print("- No data available. Please input data first.")

        case "5":
            # Sorting option for the user
            while True:
                print("\nChoose Sorting Option:")
                print("1. Ascending")
                print("2. Descending")
                print("3. Back to Main Menu")

                sort_choice = input("Enter your choice: ")

                match sort_choice:
                    case "1":
                        # Sort in ascending order
                        number_in_ascending(user_list)
                    case "2":
                       # Sort in Descending order

                        number_in_descending(user_list)
                    case "3":
                        # Go back to the main menu
                        break

        case "6":
            print("Dataset Statistics:")
            if user_list:  # Check if the list is not empty
                min_value, max_value, sum_value, avg_value = Statistics_number(user_list)
                print(f"- Minimum Value: {min_value}")
                print(f"- Maximum Value: {max_value}")
                print(f"- Sum of All Values: {sum_value}")
                print(f"- Average Value: {avg_value}")
            else:
                print("- No data available. Please input data first.")

        case "7":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        
        case _:
            print("Invalid choice. Please enter a valid choice.")
