# Non-OOP
# Bank 2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print('       Name', accountName)
    print('       Balance:', accountBalance)
    print('       Password: ', accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect Password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount.')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None

    accountBalance = accountBalance + amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount.')
        return None

    if password != accountPassword:
        print('Incorrect Password')
        return None

    if amountToWithdraw > accountBalance:
        print('Insufficient funds.')
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount("Joe", 100, 'soup')

while True:
    print()
    print('Press b to get your balance.')
    print('press d to deposit into your account')
    print('Press w to withdraw from your account.')
    print('Press s to show the account.')
    print('Press q to quit')
    print()

    action = input('What do you want to do?')
    action = action.lower() # Force to lowercase
    action = action[0] # Use first letter
    print()

    if action == 'b':
        print('Get balance:')
        userPassword = input('Please enter your password.')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is ' + theBalance)

    elif action == 'd':
        print('Deposit')
        userDepositAmount = input('Please enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        if userDepositAmount < 0:
            print('You cannot deposit a negative amount.')

        elif userPassword != accountPassword:
            print('Incorrect password')

        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is: ', accountBalance)

    elif action == 's':
        print('Show')
        print('      Name', accountName)
        print('      Balance:', accountBalance)
        print('      Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount.')

        elif userPassword != accountPassword:
            print('Wrong password')

        elif userWithdrawAmount > accountBalance:
            print('Account balance to low.')

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is: ', accountBalance)

print('Done')