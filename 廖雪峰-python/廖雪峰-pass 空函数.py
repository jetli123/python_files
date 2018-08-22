# -*- coding: utf-8 -*-
# -*- pass 返回空，用来作为占位符 -*-
def nop():
    pass

print nop()

# -*- if 语句加入 pass 什么也不干，不 return 其他结果 -*-
age = input("Enter your age: ")
if age > 18:
    pass
else:
    print('You are yong!')
