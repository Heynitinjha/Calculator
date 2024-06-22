logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def sum(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


func = {"+": sum, "-": sub, "*": mul, "/": divide}


def calculator():
    n1 = float(input("Enter the first number :"))
    for symbol in func:
        print(symbol)
    operation = input("chose the operation")

    should_continue = True
    while should_continue:

        n2 = float(input("Enter the second number:"))

        cal_func = func[operation]
        answer = cal_func(n1, n2)

        print(f"{n1} {operation} {n2} = {answer}")
        # n3 = int(input("Enter the number:"))
        # operation =input("chose the operation")
        # cal_func=func[operation]
        # answer2 = cal_func(answer,n3)
        # print(answer2)

        if input("Enter yes to continue and no to exit") == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()