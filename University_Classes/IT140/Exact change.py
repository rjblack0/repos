total_change = int(input())

if total_change <= 0:
    print('No change')

num_dollars = total_change // 100
total_change %= 100

num_quarters = total_change // 25
total_change %= 25

num_dimes = total_change // 10
total_change %= 10

num_nickels = total_change // 5
total_change %= 5

num_pennies = total_change

if num_dollars > 0:
    print(num_dollars, end=' ')
    if num_dollars == 1:
        print('Dollar')
    else:
        print('Dollars')

if num_quarters > 0:
    print(num_quarters, end=' ')
    if num_quarters == 1:
        print('Quarter')
    else:
        print('Quarters')

if num_dimes > 0:
    print(num_dimes, end=' ')
    if num_dimes == 1:
        print('Dime')
    else:
        print('Dimes')

if num_nickels > 0:
    print(num_nickels, end=' ')
    if num_nickels == 1:
        print('Nickel')
    else:
        print('Nickels')

if num_pennies > 0:
    print(num_pennies, end=' ')
    if num_pennies == 1:
        print('Penny')
    else:
        print('Pennies')