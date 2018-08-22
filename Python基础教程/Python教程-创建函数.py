def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result
abc = raw_input('Enter your number: ')
abc = int(abc)
print fibs(abc)

def hon(x, y):
    return x**y
print hon(10, 2)
