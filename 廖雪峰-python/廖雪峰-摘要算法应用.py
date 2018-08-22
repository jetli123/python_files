# -*- coding:utf-8 -*-
import hashlib


d = {
    'e10adc3949ba59abbe56e057f20f883e',  # 123456
    '21232f297a57a5a743894a0e4a801fc3',  # admin
    '5f4dcc3b5aa765d61d8327deb882cf99',  # password
    '63a9f0ea7bb98050796b649e85481845'  # root
}

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

a = calc_md5(raw_input('Enter your password: '))
print a
if a in d:
    print 'True.'
else:
    print 'False.'