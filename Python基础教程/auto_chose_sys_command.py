# -*- coding: utf-8 -*-
"""
1. Automatic selection instruction execution
2.
"""
import psutil
import paramiko
import sys
import os
import datetime


def free():
    print "system memory is: ", psutil.virtual_memory()

def cpu():
    print "system cup info: ", psutil.cpu_count(logical=False)

def hard():
    print "system hard info: ", psutil.disk_partitions()

def copy():
    hostname = '127.0.0.1'
    username = 'root'
    password = 'centos'
    port = 22

    path1 = '/root/nginx1.conf'
    path2 = '/data/nginx1.conf'
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(path1, path2)
    print "Execute success."
    sftp.close()

def ssh():
    hostname = '127.0.0.1'
    username = 'root'
    password = 'centos'
    port = 22
    password_info = '\'s password:'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    stdin, stdout1, stderr = ssh.exec_command('mkdir /data')
    stdin, stdout, stderr = ssh.exec_command('ls -lrt /data')
    print stdout1.read()
    print stdout.read()
    ssh.close()


def print_help():
    """
    If you don't know input anything. Please look up this example.
    """
    print "The available commands are: "
    print " " * 5 + "system: Check system info."
    print " " * 5 + "copy  : Execute scp file to an another server."
    print " " * 5 + "ssh   : Login to a server and execute a command."
    print " " * 5 + "?     : Print all message."


def sys_command():
    """
    Show something system command that you can execute.
    """
    print "The available commands are:"
    print " " * 5 + "free: Check system memory."
    print " " * 5 + "cpu : Check system cpu info."
    print " " * 5 + "hard: System hard space."
    print " " * 5 + "?   : Print help message."

def enter_command():
    cmd = raw_input("Enter your command (? for help): ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    try:
        while True:
            cmd = enter_command()
            if cmd == 'system':
                sys_commands = raw_input("angin your command (? for help): ")
                if sys_commands == "free":
                    free()
                elif sys_commands == "cpu":
                    cpu()
                elif sys_commands == "hard":
                    hard()
                elif sys_commands == "?":
                    print sys_command()
                elif sys_commands == "quit":
                    return
            elif cmd == "copy":
                copy()
            elif cmd == "ssh":
                ssh()
            elif cmd == "?":
                print print_help()
            elif cmd == "quit":
                return
    except Exception:
        pass

if __name__ == '__main__':

    main()
