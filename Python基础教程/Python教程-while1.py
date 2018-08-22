
while True:
    word =  raw_input('Please enter a word: ')
    if not word or word.isspace():
        print 'The word is empty'
        break
    print 'The word was ' + word

from math import sqrt
for n in range(84, 80, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
    else:
        print n
        print "Didn't find it!"

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
    print letterGirls
    #print letterGirls[boys[0]]
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
