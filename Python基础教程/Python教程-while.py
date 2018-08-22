name = ''
while not name or name.isspace():
    name = raw_input('Please enter your name: ')
print 'Hello, %s!' % name

words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print word

for digit in range(1,10):
    print digit

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'

for nam, agg in zip(names, ages):
    print nam, 'is', agg, 'years old'

