import requests
import xml.etree.ElementTree as ET

feed = requests.get('http://blog.xusheng.online/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''

     __   __  ___     _______  __   __  _______  ______    _______      __  
    |  | |  ||   |   |       ||  | |  ||       ||    _ |  |       |    |  | 
    |  |_|  ||   |   |_     _||  |_|  ||    ___||   | ||  |    ___|    |  | 
    |       ||   |     |   |  |       ||   |___ |   |_||_ |   |___     |  | 
    |       ||   |     |   |  |       ||    ___||    __  ||    ___|    |__| 
    |   _   ||   |     |   |  |   _   ||   |___ |   |  | ||   |___      __  
    |__| |__||___|     |___|  |__| |__||_______||___|  |_||_______|    |__| 


## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](http://blog.xusheng.online/archives/)
''')
