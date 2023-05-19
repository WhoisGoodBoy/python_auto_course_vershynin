from xml.etree import ElementTree

'''
print(collection)
with open('example.xml', 'r') as e:
    tostr_example = e.read()
    result = ElementTree.fromstring(tostr_example)
    print(result)
    print(type(result))
'''
#for genre in collection:
#    for decade in genre:
#        print(decade.tag)
#print(ElementTree.tostring(collection).decode())

tree = ElementTree.parse('example.xml')
collection = tree.getroot()
for movie in collection.iter('movie'):
    print()
    for child in movie.findall('*'):
        print({child.tag:child.text})
