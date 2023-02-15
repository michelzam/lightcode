# Calculate the quotient



def main():
    # get user input
    dividend = int(input("Divident: "))
    divisor = int(input("Divisor: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"{dividend = }")
    print(f"{remainder = }")

main()

