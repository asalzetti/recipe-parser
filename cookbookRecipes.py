from pathlib import Path
from xml.dom.minidom import parseString



p = Path('C:\\Python36\\cookbook_textencoded')
numb = 0
for x in p.iterdir():
    if x.is_file():
        file = open(str(x), 'r')
        data = file.read()
        file.close()
        dom = parseString(data)
        numb += len(dom.getElementsByTagName('recipe'))
        for item in dom.getElementsByTagName('recipe'):
            name = item.getElementsByTagName('purpose')[0]
            try:
                print(name.firstChild.data)
            except:
                pass
print(numb)
