import xml.etree.ElementTree as ET
import os
def read_content(xml_file: str):
    def remove(x):
        return x.replace("'", "")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    list_with_all_boxes =[]
    for boxes in root.iter('object'):
        filename = os.path.basename(xml_file)
        filename=filename.replace('.xml','.jpg')
        name = filename.strip('.xml')
        label = None
        ymin,xmin,ymax,xmax = None,None,None,None

        ymin = int(boxes.find('bndbox/ymin').text)
        xmin = int(boxes.find('bndbox/xmin').text)
        ymax = int(boxes.find('bndbox/ymax').text)
        xmax = int(boxes.find('bndbox/xmax').text)
        label = boxes.find('name').text
        list_with_single_boxes = [xmin, ymin, xmax, ymax, label]
        list_with_all_boxes.append(list_with_single_boxes)

    return filename, list_with_all_boxes,name



list_dir = os.listdir('D:\\HK1-2020-2021\\Machine-Learning-Statistics\\OD\\UIT-VD\\Train')
path =  'D:\\HK1-2020-2021\\Machine-Learning-Statistics\\OD\\UIT-VD\\Train'

list_dir_xml = []
for i in list_dir:
    if i.endswith(".xml"):
        list_dir_xml.append(i)

for i in list_dir_xml:
    filename,boxes,name = read_content(os.path.join(path,i))
    path_dir = 'E:/train2'
    name = name.strip('.jpg')
    files = name+'.txt'
    with open(os.path.join(path_dir, files), 'w') as fp:
        for j in boxes:
            fp.write(str(j).strip("[]'"))
            fp.write('\n')

