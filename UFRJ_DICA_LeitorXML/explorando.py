import xml.etree.ElementTree as ET

tree = ET.parse("lesson.xml")
root = tree.getroot()

#for child in root:
    #print(child.tag, child.attrib,child.text,child.tail)

print("\n")

for neighbor in root.iter('lesson'):
    for child in neighbor:
        for pages in child.iter('pages'):
            for child_2 in pages:
                #print(child_2.tag,child_2.attrib,child_2.text)
                for child_3 in child_2:
                    #...
                    #print(child_3.tag,child_3.attrib,child_3.text)
                    for child_4 in child_3:
                        #print(child_4.tag,child_4.attrib,child_4.text)
                        for child_5 in child_4:
                            #print(child_5.tag,child_5.attrib,child_5.text)
                            for child_6 in child_5:
                                #print(child_6.tag,child_6.attrib,child_6.text)
                                for child_7 in child_6:
                                    #print(child_7.tag,child_7.attrib,child_7.text)
                                    #...