# Cashier Challenge

# Input
# Int
# Number under dollar

# Output
# String to describe how to pass out change.

def change_back(money_in):
    quarters = money_in // 25
    money_left = money_in % 25
    dimes = money_left // 10
    money_left = money_left % 10
    nickels = money_left // 5
    money_left = money_left % 5 # pennies = money_left at this point

    print(f'Your change of {money_in}¢ will be given with {quarters} quarters, {dimes} dimes, {nickels} nickels, and {money_left} pennies')

my_change = int(input('How much change are you getting back? '))
change_back(my_change)
    