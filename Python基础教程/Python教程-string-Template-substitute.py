strit = "Hello, %s. %s you?"
values = ('World', 'Are')
print strit % values

from string import Template
s = Template("$ar are you $br?")
d={}
d['ar'] = 'Where'
d['br'] = 'from'
s.substitute(d)
s = Template('$x are you?')
s.substitute(x='Where')
s = Template("How ${x}ch?")
s.substitute(x='mu')
from math import pi
'Pi: %f...' % pi

