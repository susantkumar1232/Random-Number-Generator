import random  # Importing the random module

def generate_random_numbers(count, start, end):
    random_numbers = [random.randint(start, end) for _ in range(count)]
    return random_numbers

if __name__ == "__main__":
    print("Random Number Generator")
    
    try:
        count = int(input("Enter the number of random numbers you want to generate: "))
        start = int(input("Enter the starting range: "))
        end = int(input("Enter the ending range: "))

        if start > end:
            print("Invalid range! Starting range should be less than or equal to the ending range.")
        else:
            random_numbers = generate_random_numbers(count, start, end)
            print("\nGenerated Random Numbers:")
            for num in random_numbers:
                print(num)
    except ValueError:
        print("Invalid input! Please enter valid integers.")
      
