def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i:<2} = {result}")


def print_tables_up_to_n(n):
    for number in range(1, n + 1):
        print_single_table(number)
        print("-" * 29)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print_single_table(number)

    print() 


    n = int(input("Enter N (tables from 1 to N): "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)