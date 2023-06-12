def main():
    total_sum = 0
    while total_sum < 1000:
        try:
            input_number = int(input("Enter a positive integer (or a negative number to stop): "))
            if input_number <= 0:
                break
            total_sum += input_number
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    print("Exiting the program.")
    print("Final sum:", total_sum)


if __name__ == "__main__":
    main()

