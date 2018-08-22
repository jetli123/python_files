people = {
    'Alice': {
        'phone': '2341',
        'addR': 'Foo drive 23'
    },
    'Beth': {
        'phone': '4902',
        'addR': 'Bar street 42'
    },
    'Cecil': {
        'phone': '4355',
        'addR': 'Baz avenue 30'
    }
}
"""
For phone number and address to used.
"""
labels = {
    'phone': 'phone number',
    'addR': 'address'
}
names = raw_input('Name: ')
"""
Find phone number or address?
"""
request = raw_input('Phone number (p) or address (a)? ')
"""
used correct key:
"""
if request == 'p':
    keys = 'phone'
if request == 'a':
    keys = 'addR'
"""
if name exist in people of dictionary, then print key.
"""
if names in people:
    print "%s's %s is %s." % (names, labels[keys], people[names][keys])
else:
    print "%s not exist %s." % (names, people)
