seq = ['1', '2', '3', '4', '5']
print '+'.join(seq)
sed = ['', 'usr', 'bin', 'local', '']
print 'C:' + '\\'.join(sed)

if 'User'.lower() in ['user', 'admin', 'nokia']:
    print 'Found it'
else:
    print 'Not found'

print 'hollow,world i like you'.title()

s = 'How are you? I\'m fine.'
print s.find('How', 0, 12)

import string
print string.capwords("that's all, folks")

print 'January February March April May June July August September October November December'.split()

print '1+2+3+4+5'.split('+')
print '/usr/local/zabbix/etc'.split('/')
print 'name create_time ne_type id'.split()

print '*** Hollow World !! ##'.strip('* !#')

names = ['admin', 'nokia', 'systemadmin']
if ' admin '.strip(' ') in names: print 'Found it'
else: print 'Not found'
