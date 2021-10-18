acceptable_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tic_tac = {}


def user_input(i):
    user = "string"
    check = False
    """"
    Taking input from the user and validating the conditions.
    validations:
    1. Accept only if the input is integer
    2. Accept if the input is in acceptable_inputs range
    """
    if i in range(1, 10, 2):  # 1,3,5,7,9
        while user.isdigit() == False or check == False:
            user = input(f"{i}user1 - Enter a number of your choice(1-9): ")
            if user.isdigit() == False:
                print("Enter a valid number")
                continue
            if int(user) in acceptable_inputs:
                check = True
        tic_tac[user] = 'O'
        acceptable_inputs[int(user)] = ' '
    elif i in range(2, 10, 2):
        while user.isdigit() == False or check == False:
            user = input(f"{i}user2 - Enter a number of your choice(1-9): ")
            if user.isdigit() == False:
                print("Enter a valid number")
                continue
            if int(user) in acceptable_inputs:
                check = True
        tic_tac[user] = 'X'
        acceptable_inputs[int(user)] = ' '


for i in range(1, 10):
    user_input(i)
lists = tic_tac.values()
ls = list(lists)
for i in range(3):
    print("{} {} {}".format(*ls[3 * i:3 * i + 3]))
