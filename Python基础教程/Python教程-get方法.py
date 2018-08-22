labels = {
    'phone': '110-02034',
    'addr': 'Beijing'
}
name = raw_input('Name: ')
request = raw_input('Phone number (p) or address (a)? ')
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
label = labels.get(key)
result = labels.get(key, 'key')
print "%s's %s is %s." % (name, label, result)
