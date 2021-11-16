#!/usr/bin/python
import re
import glob
import codecs
from bs4 import BeautifulSoup

for html in glob.iglob('*.html', recursive=True):
        origin_file = open(html)
        page = origin_file.read()
        soup = BeautifulSoup(page, 'html.parser')
        s = soup.prettify()
        s = re.sub('(?<=[a-z])\-\- ', ' — ', s)
        output = "../output/" + html

        f = codecs.open(output, encoding='utf-8', mode='w+')
        f.write(s)
        f.close()
        origin_file.close()                
