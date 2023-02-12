
def number3(number1_, number2_):
    if number1_ > number2_:
        print(f"The bigger number is {number1_}")
    else:
        if number2_ > number1_:
            print(f"The bigger number is {number1_}")


def numbercheck(number1_, number2_):
    if number1_ == number2_:
        return [False, "The numbers are equal"]

    else:
        return [True, ""]





while True:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))

    except ValueError:
        print("Invalid number"
              "please enter a number")
    result = numbercheck(number1, number2)
    if result[0] is False:
        print(result[1])
        break
    else:
        print("Valid number")
    print(f"Result: Good")
    number3(number1, number2)






