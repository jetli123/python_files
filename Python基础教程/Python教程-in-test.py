users = ['admin', 'test', 'nok']
cc = raw_input("Please enter the username: ")
if cc in users:
    print 'The user is true,it\'s being login!'

database = [
    ['admin', '123'],
    ['scoot', '456'],
    ['sys', '888888']
]
name = raw_input("Enter login name: ")
pas = raw_input("Enter login password: ")
if [name, pas] in database:
    print "User and Password is true,please login server."
else:
    print "User and Password is failed!"
