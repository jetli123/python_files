print '+' + '-' * 30 + '+'
print '|' + ' ' * 30 + '|'
print '|' + ' ' * 8 + 'He is a very good boy!' + '|'
print '+' + '-' * 30 + '+'
varchar = raw_input("The value: ")
scr = 80
test = len(varchar)
box = test + 6
left = (scr - box) / 2
print
print ' ' * left + '+' + '-' * (box - 2) + '+'
print ' ' * left + '|' + ' ' * test + '|'
print ' ' * left + '|' + '    ' + varchar + '       ' + '|'
print ' ' * left + '|' + ' ' * test + '|'
print ' ' * left + '+' + '-' * (box - 2) + '+'
