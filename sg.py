from xml.dom import minidom
import xml.etree.ElementTree as ET

filePath = "/Users/ls/Desktop/古诗/123.xml"

tree = ET.parse(filePath)

root = tree.getroot()

for pElements in root.iter('p'):
    print(pElements.text)
    # for ele in pElements.iter():
    #     # if len(ele) > 0:
    #     if ele.text != "None":
    #     print(ele.text)




# for child in root:
#     # print(child.tag,":",child.attrib)
#     for children in child:
#         # print(children.tag,":",children.attrib)
#         for grandChildren in children:
#             if grandChildren.tag == "p":
#                 # if grandChildren.tag.hasChild:
#                 print(grandChildren.text)
#                 if grandChildren.getChildren






# dom = minidom.parse(filePath)
# root = dom.getroot()
# # # print(root.nodeName)
# # # print(root.nodeValue)
# # ps = dom.getElementsByTagName("p")
# for i in range(len(ps)):
#     print(ps[i].text)
# for child in root:
#     print(child.tag)
