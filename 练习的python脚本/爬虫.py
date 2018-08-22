# -*- coding: utf-8 -*-
import urllib2
import re
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


def xs():
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    URL = 'http://www.quanshuwang.com/book/11/11259'
    request = urllib2.Request(URL, headers=header)
    get1 = urllib2.urlopen(request, timeout=3)
    abc = get1.read().decode('gbk')
    a = re.compile(r'<li><a href="(.*?)" title="(.*?)">.*')
    line = a.findall(abc)

    i = 1
    for lines in line:
        if i > 50:
            break
        else:
            no_url = lines[0]
            no_tital = lines[1].split('，')
            no_tital = no_tital[0]
        #   print no_url, no_tital
            headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
            request = urllib2.Request(no_url, headers=headers)
            gets = urllib2.urlopen(request)
        # ab = unicode(gets.read(), 'GBK').encode('utf-8')
            ab = gets.read().decode('gbk')
            reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # re.S 多行匹配
            reg = re.compile(reg, re.S)
            words = reg.findall(ab)
            words = words[0].replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
            words = words.replace('<br />', '').strip('')
        # print words
            f = open(r'C:/Users/JETLI/Desktop/xiaoshuo/{}.txt'.format(no_tital).encode('gbk'), 'w')
            f.write(words.decode('utf-8'))
            print '备份章节： %s' % no_tital
            f.close()
            time.sleep(8)
        i += 1

if __name__ == '__main__':
    xs()