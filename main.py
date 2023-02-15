# :smile: Calculate the quotient

def calculate_quotient():
    # get user input
    dividend = int(input("Divident: "))
    divisor = int(input("Divisor: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"{dividend = }")
    print(f"{remainder = }")

    return remainder

def accumulate():
    # housekeeping
    acumulator = 0

    for i in range(5):
        print(f"Collecting integer pair {i + 1}")
        acumulator += calculate_quotient()

    print(f"{acumulator = }")

def main():
    # main loop

    accumulate()

main()
