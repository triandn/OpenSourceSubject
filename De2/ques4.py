def find_power_using_lambda():
    power = lambda numberOne,numberTwo: numberTwo and numberOne * power(numberOne,numberTwo - 1) or 1

    numberOne = int(input('Input x: '))
    numberTwo = int(input('Input y: '))

    print('power(%d,%d)= %d' %(numberOne, numberTwo, power(numberOne,numberTwo)))
    
find_power_using_lambda()