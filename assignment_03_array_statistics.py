def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


if __name__ == "__main__":
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = []
        for i in range(n):
            value = int(input(f"Enter number {i + 1}: "))
            numbers.append(value)

        total = calculate_sum(numbers)
        average = calculate_average(numbers)
        maximum = find_maximum(numbers)
        minimum = find_minimum(numbers)

        print("\nResults:")
        print(f"Sum:     {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")


