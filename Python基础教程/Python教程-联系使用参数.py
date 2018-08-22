def story(**kwds):
    return 'Once upon a time,there was a ' '%(job)s called %(name)s. ' % kwds

def power(x, y, *others):
    if others:
        print 'Received parameters: ', others
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step >0'
    if stop is None:
        start, stop = 0, start
    #print start, stop
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print story(job='king', name='Gumby')
#print story(name='Sir Robin', job='brave knight')
params = {'job': 'language', 'name': 'Python'}
print story(**params)
del params['job']
print params
print story(job='stroke of genius', **params)

print power(2, 3, 'ndn', 2)
print power(x=3, y=2)
params = (5,) * 2
print power(*params)
print power(3, 3, 'Hello, world')

print interval(10)
print interval(1, 5)
print interval(3, 12, 4)
print power(*interval(3, 7))
raw_input("Enter any keybord to next: ")
