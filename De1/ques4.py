def find_factorial_using_lambda():
    factorial = lambda num : 1 if num <= 1 else num*factorial(num-1)

    number = int(input('Input number: '))

    print('%d != %d' %(number, factorial(number)))

find_factorial_using_lambda()