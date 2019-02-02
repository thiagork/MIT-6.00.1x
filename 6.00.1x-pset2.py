# MIT 6.00.1x
# Problem Set 2


def calculateBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Calculates the credit card balance after one year if
    a person only pays the minimum monthly payment required by the credit card
    company each month.
    Prints the result to console.
    Doesn't return any value.

    Input:
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
        monthlyPaymentRate - minimum monthly payment rate as a decimal
    '''
    for i in range(12):
        print(balance)
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        interest = unpaidBalance * annualInterestRate / 12
        balance = round((unpaidBalance + interest), 2)
    print(balance)


def minimumFixedPayment(balance, annualInterestRate):
    '''
    Calculates the minimum fixed(does not change each month) monthly payment
    needed in order pay off a credit card balance within 12 months.
    Prints the lowest monthly payment that will pay off all debt in 1 year.
    Doesn't return any value.

    Input:
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
    '''
    fixedPayment = 10
    updatedBalance = balance

    while updatedBalance >= 0:
        updatedBalance = balance
        fixedPayment += 10
        for i in range(12):
            unpaidBalance = updatedBalance - fixedPayment
            interest = unpaidBalance * annualInterestRate / 12
            updatedBalance = unpaidBalance + interest


def minimumFixedPaymentBisectionSearch(balance, annualInterestRate):
    '''
    Using Bisection Search, calculates the minimum fixed(does not change each
    month) monthly payment.
    needed in order pay off a credit card balance within 12 months.
    Prints the lowest monthly payment that will pay off all debt in 1 year.
    Doesn't return any value.

    Input:
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
    '''
    monPayLower = balance / 12
    monPayUpper = balance * ((1 + annualInterestRate/12)**12) / 12
    while True:
        fixedPayment = (monPayLower + monPayUpper) / 2
        updatedBalance = balance
        for i in range(12):
            unpaidBalance = updatedBalance - fixedPayment
            interest = unpaidBalance * annualInterestRate / 12
            updatedBalance = round((unpaidBalance + interest), 2)
        if updatedBalance > 0:
            monPayLower = fixedPayment
        elif updatedBalance < 0:
            monPayUpper = fixedPayment
        elif updatedBalance == 0:
            break
    print(round(fixedPayment, 2))
