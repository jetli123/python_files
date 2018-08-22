width = input("Please enter width: ")
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
Format = '%-*s%*.2f'
print '=' * width
print header_format % (item_width, 'Item', price_width, 'Price')
print '-' * width
print Format % (item_width, 'Apples', price_width, 0.4)
print Format % (item_width, 'Banana', price_width, 4.0)
print Format % (item_width, 'Orange', price_width, 3.2)
print Format % (item_width, 'Prunes (4 lbs.)', price_width, 0.34)
print Format % (item_width, 'Pineapple (16 oz.)', price_width, 8.5)
