def hello_3(greeting = 'Hello', name = 'world'):
    print '%s, %s' % (greeting, name)

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)

def add(x, y):
    return x + y

param = (1, 2)
print add(*param)

def ab(*name):
    obc = name
    return obc

print ab('cc', 'nd')

def AB(**parm):
    print parm

AB(x = 1, y = 2, z = 3)

def with_stars(**kwds):
    print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
    print kwds['name'], 'is', kwds['age'], 'years old'
args = {'name': 'Mr Gumby', 'age': 110}
with_stars(**args)
without_stars(args)