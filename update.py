import requests
import xml.etree.ElementTree as ET

feed = requests.get('http://blog.xusheng.online/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''

  _    _   ______   _        _         ____                 _   _   _____    _____     ____    _____   _____  
 | |  | | |  ____| | |      | |       / __ \        /\     | \ | | |  __ \  |  __ \   / __ \  |_   _| |  __ \ 
 | |__| | | |__    | |      | |      | |  | |      /  \    |  \| | | |  | | | |__) | | |  | |   | |   | |  | |
 |  __  | |  __|   | |      | |      | |  | |     / /\ \   | . ` | | |  | | |  _  /  | |  | |   | |   | |  | |
 | |  | | | |____  | |____  | |____  | |__| |    / ____ \  | |\  | | |__| | | | \ \  | |__| |  _| |_  | |__| |
 |_|  |_| |______| |______| |______|  \____/    /_/    \_\ |_| \_| |_____/  |_|  \_\  \____/  |_____| |_____/ 
                                                                                                              
                                                                                                              
## Latest blog posts
''')
    for entry in root.findall('nsfeed:entry', nsfeed)[:5]:
        text = entry.find('nsfeed:title', nsfeed).text
        url = entry.find('nsfeed:link', nsfeed).attrib['href']
        published = entry.find('nsfeed:published', nsfeed).text[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](http://blog.xusheng.online/archives/)

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=xshengcn)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=xshengcn&hide=ipynb,html&layout=compact)
''')
