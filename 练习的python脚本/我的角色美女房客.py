# -*- coding: utf-8 -*-

import urllib2
import re
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def xs():
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    URL = 'http://www.biqukan.com/30_30980'
    request = urllib2.Request(URL, headers=header)
    get1 = urllib2.urlopen(request, timeout=10)
    abc = get1.read().decode('gbk')

    # 从本地访问
    # with open(r'C:/Users/JETLI/Desktop/fangke.txt') as f:
    #     abc = f.read().decode('utf-8')
    # -*-

    a = re.compile(r'<dd><a href ="(.*?)">(.*?)</a>.*')
    line = a.findall(abc)
    i = 1
    for lines in line:
        if i > 30:
            break
        elif 0 <= i < 20:
            no_url = 'http://www.biqukan.com'+lines[0]
            no_title = lines[1]
            # print no_url, no_title
            headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
            request = urllib2.Request(no_url, headers=headers)
            gets = urllib2.urlopen(request, timeout=3)
            ab = gets.read().decode('gbk')
            reg = r'showtxt">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(.*)http://www.biqukan.com'
            # re.S 多行匹配
            reg = re.compile(reg, re.S)
            words = reg.findall(ab)
            old_word = words[-1].replace('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', '').replace(
                '<br />', ''
            ).encode('utf-8')
            f = open(r'C:/Users/JETLI/Desktop/meinv/{}.txt'.format(no_title).encode('gbk'), 'w')
            f.write(old_word.encode('utf-8'))
            print '备份章节： %s' % no_title
            f.close()
            time.sleep(15)
        i += 1

if __name__ == '__main__':
    xs()
    print(u'备份完成退出程序')
    time.sleep(3)
