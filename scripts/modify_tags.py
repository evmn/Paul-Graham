#!/usr/bin/python
import re
import glob
import codecs
from bs4 import BeautifulSoup

TEMPLATE = u'<html lang="en"><head><title>{0}</title></head><body>{1}</body></html>'
H1 = '<h1>{0}</h1>'

#with open("gt.html") as page:
#        soup = BeautifulSoup(page, 'html.parser')
for html in glob.iglob('*.html', recursive=True):
        origin_file = open(html)
        page = origin_file.read()
        soup = BeautifulSoup(page, 'html.parser')
        title = soup.title.getText()
        content = soup.find('td', width="435")
        if content:
                s = content.prettify()
                s = re.sub('<br/>\s*<br/>', '</p><p>', s)
                s = re.sub('<font[^>]*>|</font>|<br>|</br>|<br/>|<td[^>]*>|</td>|</img>','',s)
                s = re.sub('<img[^>]*>\s*</p>',str.format(H1, title),s)

                tag_table = re.compile('<table.*</table>', re.DOTALL)
                s = re.sub(tag_table, '', s)
                s = TEMPLATE.format(title,s)
                soup = BeautifulSoup(s, 'html.parser')
                output = "../output/" + html
                f = codecs.open(output, encoding='utf-8', mode='w+')
                f.write(soup.prettify())
                f.close()
        else:
                print(html)
        origin_file.close()                
        
