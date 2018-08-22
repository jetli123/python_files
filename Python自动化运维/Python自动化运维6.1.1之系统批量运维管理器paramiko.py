# -*- coding: utf-8 -*-
"""paramiko 支持 pip、easy_install 或源码安装方式，解决了包依赖的问题"""
# pip install paramiko
# easy_install paramiko
# paramiko 依赖第三方的 Crypto、Ecdsa 包及Python 开发包python-devel 的支持，源码安装步骤如下：
# yum -y install python-devel
# wget http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-2.6.tar.gz
# tar -zxvf pycrypto-2.6.tar.gz
# cd pycrypto-2.6
# python setup.py install
# cd ..
# wget https://pypi.python.org/packages/source/e/ecdsa/ecdsa-0.10.tar.gz --no-check-certificate
# tar -zxvf ecdsa-0.10.tar.gz
# cd ecdsa-0.10
# python setup.py install
# cd ..
# wget https://github.com/paramiko/paramiko/archive/v1.12.2.tar.gz
# tar -zxvf v1.12.2.tar.gz
# cd paramiko-1.12.2/
# python setup.py install

"""依赖包：
asn1crypto-0.24.0
bcrypt-3.1.4
cffi-1.11.5
cryptography-2.3
enum34-1.1.6
ipaddress-1.0.22
paramiko-2.4.1
pyasn1-0.4.4
pycparser-2.18 pyna
cl-1.2.1
six-1.11.0"""
import paramiko

