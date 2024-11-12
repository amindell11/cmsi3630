def main():
    # Prompt the user for input
    input_string = input("Enter a space-delimited list of numbers: ")
    
    # Split the input string on spaces to get the numbers
    numbers = input_string.split()
    
    # Convert the list of string numbers to integers
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        print("Please ensure all inputs are valid integers.")
        return  # Exit the function on error

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Convert the sum to a binary string
    binary_representation = bin(total_sum)[2:]  # Skip the '0b' prefix
    
    # Print the result
    print(f"The sum of the provided numbers as a binary string is: {binary_representation}")

if __name__ == "__main__":
    main()
