# -*- coding:utf-8 -*-

import urllib
import re
import xlwt
from bs4 import BeautifulSoup
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

html = open('e:/test/index.html').read()
soup = BeautifulSoup(html, "html.parser")
text = soup.prettify()

txt = open('e:/test/index.htmlll.txt', 'w')
txt.write(text)
txt.close()
print 'ok'

