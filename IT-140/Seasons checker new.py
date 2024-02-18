month = input()
day = int(input())

if month == 'January' and 0 < day <= 31:
    print ('Winter')

elif month == 'February' and 0 < day <= 29:
    print('Winter')

elif month == 'March':
    if day > 0 and day <= 19:
        print('Winter')
    elif day > 19 and day <= 31:
        print('Spring')
    else:
        print('Invalid')
elif month == 'April' and 0 < day <= 30:
    print ('Spring')

elif month == 'May' and 0 < day <= 31:
    print('Spring')

elif month == 'June':
    if 0 < day <= 20:
        print('Spring')
    elif 20 < day <= 30:
        print('Summer')
    else:
        print('Invalid')

elif month == 'July' and 0 < day <= 31:
    print ('Summer')

elif month == 'August' and 0 < day <= 31:
    print ('Summer')

elif month == 'September':
    if 0 < day <= 21:
        print('Summer')
    elif 21 < day <= 30:
        print('Autumn')
    else:
        print('Invalid')

elif month == 'October' and 0 < day <= 31:
    print ('Autumn')

elif month == 'November' and 0 < day <= 30:
    print ('Autumn')

elif month == 'December':
    if 0 < day <= 20:
        print('Autumn')
    elif 20 < day <= 31:
        print('Winter')
    else:
        print('Invalid')

else:
    print('Invalid')