# Define your function here
def exact_change(user_total):
    # Converts to dollars
    num_dollars = user_total // 100
    # Checks to see how many dollars are remaining
    user_total = user_total - (num_dollars * 100)

    # Converts to quarters
    num_quarters = user_total // 25
    # Checks to see how many quarters are remaining
    user_total = user_total - (num_quarters * 25)

    # Converts to dimes
    num_dimes = user_total // 10
    # Checks to see how many dimes are remaining
    user_total = user_total - (num_dimes * 10)

    # Converts to nickels
    num_nickels = user_total // 5
    # Checks to see how many nickles are remaing
    user_total = user_total - (num_nickels * 5)

    # Converts to pennies
    num_pennies = user_total // 1
    user_total = user_total - (num_pennies * 1)

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input('Enter change '))
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Type your code here
    # Checks to see if user input is 0 if so output no change
    if input_val == 0:
        print('no change')
    # Checks to see if the user input for dollars,quarters,dimes,nickels,pennies, output needs to be singular or plural
    else:
        # If dollar is greater than one
        if num_dollars > 1:
            # Print number of dollars
            print(num_dollars, 'dollars')
        # If dollar is equal to one
        elif num_dollars == 1:
            # Print one dollar
            print(num_dollars, 'dollar')
        # If quarters is greater than one
        if num_quarters > 1:
            # Print number of quarters
            print(num_quarters, 'quarters')
        # If quarters is equal to one
        elif num_quarters == 1:
            # Print one quarter
            print(num_quarters, 'quarter')
        # If dime is greater than one
        if num_dimes > 1:
            # Print number of dimes
            print(num_dimes, 'dimes')
        # If dimes is equal to one
        elif num_dimes == 1:
            # Print one dime
            print(num_dimes, 'dime')
        # If nickels is greater than one
        if num_nickels > 1:
            # Print number of nickles
            print(num_nickels, 'nickels')
        # If nickels is equal to one
        elif num_nickels == 1:
            # Print one nickels
            print(num_nickels, 'nickel')
        # If pennies is greater than one
        if num_pennies > 1:
            # Print number of pennies
            print(num_pennies, 'pennies')
        # If pennies is equal to one
        elif num_pennies == 1:
            # Print one penny
            print(num_pennies, 'penny')