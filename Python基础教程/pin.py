database = [
    ['alan', '1725'],
    ['lily', '3430'],
    ['tom', '2229']
]
username = raw_input("User name: ")
pin = raw_input("PIN code")
if [username, pin] in database:
    print 'Access granted.'
