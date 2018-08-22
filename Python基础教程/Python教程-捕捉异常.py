class SomeCustomException(Exception):
    pass

x = input('Enter the first number: ')
y = input('Enter the second number: ')
print x/y


try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print x/y
except ZeroDivisionError:
    print "The second number can't zero!"

