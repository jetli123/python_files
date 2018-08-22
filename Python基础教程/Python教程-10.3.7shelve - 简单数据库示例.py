# -*- coding: utf-8 -*-
# database.py
"""此脚本存储每月支出明细，确保每笔交易存在记录，便于查询使用"""
import shelve


def store_person(db):
    """
    Quere user for data and store it in the shelf object
    """

    pid = raw_input('Enter unique ID number: ')  # 使用人唯一ID号
    person = dict(year=raw_input('Enter Year: '), mother=raw_input('Enter mother: '),
                  address=raw_input('Enter address: '), money=raw_input('Enter your money: '))

    db[pid] = person


def lookup_person(db):
    """
    Query user for ID and desired field. And fetch the corresponding data from
    the shelf object
    """

    pid = raw_input('Enter ID  number: ')  # 输入ID 查看存在的记录
    choice = raw_input('Enter 1 or 2 (1: print all message. 2: print in of ID for person.)')
    choice = choice.strip()
    if choice == '1':
        print 'All person message :', db[pid]
    elif choice == '2':
        field = raw_input('What would you like to know? (year, mother, address, money)')
        field = field.strip().lower()
        print str(field) + ':', db[pid][field]


def print_help():
    """
    If you don't know input anything, please look up this example.
    """
    print 'The available commands are:'
    print ' ' * 5 + 'store : Store information for a person'
    print ' ' * 5 + 'lookup: Look up a person from ID number'
    print ' ' * 5 + 'quit  : Save changes and exit'
    print ' ' * 5 + '?     : Print all message'


def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('D:\\Python software\\python file\\database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__':
    main()