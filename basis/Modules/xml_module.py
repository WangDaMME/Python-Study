import xml.etree.ElementTree as ET

tree=ET.parse("gdp_xml.xml")
root=tree.getroot()
print(root.tag)

'''
# 遍历xml Traverse
for child in root:
    print(child.tag,child.attrib)  # tag：标签名 attrib 属性
    for i in child:
        print(i.tag,i.text)  # i.text <> text<> 两个>< 之间的东西
'''

# 只找自己想要的
# Transver Year
for node in root.iter('year'):
    print(node.tag, node.text)


# 修改
for node in root.iter('year'):
    new_year=int(node.text)+1  # 获取的是str
    node.text=str(new_year)
    node.set("updated_by","Michael")  #增加属性attrib

tree.write("gdp_xml.xml")  #写回源文件

#删除 root. remove
for country in root.findall('country'):
    rank=int(country.find('rank').text)
    if rank>50:
        root.remove(country)

tree.write("rem_output.xml")  #写回源文件

# Create Xml
new_xml= ET.Element("namelist")  # root
name=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})   # child element of (new_xml), "name"标签名tag， attibute 属性
age=ET.SubElement(name,"age",attrib={"checked":"no"})   # child element of (new_xml), "name"标签名tag， attibute 属性
sex=ET.SubElement(name,"sex")
age.text='22'
name2=ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age=ET.SubElement(name2,"age")
age.tex='32'

et=ET.ElementTree(new_xml)  # Create File 生成文档对象
et.write("new_create.txt",encoding="utf-8",xml_declaration=True)  # declaration: 声明 xml 1.0 version...
ET.dump(new_xml)