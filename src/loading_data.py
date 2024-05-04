import pandas as pd
import os
import xml.etree.ElementTree as ET
import cv2

def loading_data():
    annotations_dir = '../data/annotations/'
    img_dir = '../data/images/'

    img_lst = []
    label_lst = []
    img_filename = []

    for filename in os.listdir(annotations_dir):
        xml_path = os.path.join(annotations_dir, filename)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        img_name = root.find('filename').text
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)

        for obj in root.findall('object'):
            classname = obj.find('name').text
            xmin = int(obj.find('bndbox/xmin').text)
            ymin = int(obj.find('bndbox/ymin').text)
            xmax = int(obj.find('bndbox/xmax').text)
            ymax = int(obj.find('bndbox/ymax').text)
            imgbndbox = img[ymin:ymax, xmin:xmax]

            label_lst.append(classname)
            img_lst.append(imgbndbox)
        img_filename.append(img_name)
    return {'img_lst': img_lst, 'label_lst': label_lst, 'img_filename': img_filename}


