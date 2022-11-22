centimeters = float(input('Enter amount here'))
print(centimeters*0.394)
print(centimeters*0.0328)
year = int(input('Enter year here'))
remainder = year%100
remainder2 = year%400
remainder3 = year%4
if remainder == 0:
    if remainder2 == 0:
        print('This is a leap year')
    else:
        print('This is not a leap year')
else:
    if remainder3 == 0:
        print('This is a leap year')
    else:
        print('This is not a leap year')