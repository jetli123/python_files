# -*- coding: utf-8 -*-
"""
    Python 的 dict 对象可以直接序列化为 JSON 的{}，不过，很多时候，我
们更喜欢用 class 表示对象，比如定义 Student 类，然后序列化：
"""
import json


# 例子1：
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', '22', '99')
# Student 实例首先被 student2dict()函数转换成 dict，然后再被顺
# 利序列化为 JSON
print json.dumps(s, default=student2dict)

# 不过，下次如果遇到一个 Teacher 类的实例，照样无法序列化为 JSON。
# 我们可以偷个懒，把任意 class 的实例变为 dict：
print json.dumps(s, default=lambda obj: obj.__dict__)
"""
    因为通常 class 的实例都有一个__dict__属性，它就是一个 dict，用来
存储实例变量。
"""


# 例子2： 练习
class Test(object):

    def __init__(self, id, code):
        self.id = id
        self.code = code

d = Test('190', '10010')
print json.dumps(d, default=lambda cuy: cuy.__dict__)


# -- 我们要把 JSON 反序列化为一个 Student 对象实例，
# loads()方法首先转换出一个 dict 对象，然后，我们传入的 object_hook 函数
# 负责把 dict 转换为 Student 实例：

# 例子1：
def dict2student(f):
    return Student(f['name'], f['age'], f['score'])

json_str = '{"age": "22", "score": "99", "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student)
#


# 例子2：
def dict2student2(o):
    return Test(o['id'], o['code'])

json_str1 = '{"code": "10010", "id": "190"}'
print json.loads(json_str1, object_hook=dict2student2)
