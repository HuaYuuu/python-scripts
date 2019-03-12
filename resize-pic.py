import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

import cv2


classes = ["insulator1", "insulator2", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def box_resizetune(box_obj):
	box_xmin=box_obj[0]/10
	box_xmax=box_obj[1]/10
	box_ymin=box_obj[2]/10
	box_ymax=box_obj[3]/10
	return (int(box_xmin),int(box_xmax),int(box_ymin),int(box_ymax))

def readwrite1( input_file,output_file):
 f = open(input_file, 'r')
 out = open(output_file,'w')
 print (f)
 for line in f.readlines():
 a = line.split(",")
 x=a[0] + "," + a[1]+"\n"
 out.writelines(x)
 f.close()
 out.close()


def eachFile(path):
    num=0
    for parent,dirnames,filenames in os.walk(path):
	for filename in filenames:
		(myfilepath,mytempfilename) = os.path.split(os.path.join(parent,filename))
		(myfilename,extension) = os.path.splitext(mytempfilename)
		if(extension==".jpg"):
			img = cv2.imread(os.path.join(parent,filename))
			in_file = open(os.path.join(myfilepath,myfilename+".xml"))
    			tree=ET.parse(in_file)
    			root = tree.getroot()
			h,w,c= img.shape
			print("%s"%myfilename+".jpg:(h,w)"+str(h)+","+str(w))
   			for obj in root.iter('object'):
				out_file = open(labelpath+"%s.txt"%str(num), 'w')
       				difficult = obj.find('difficult').text
        			cls = obj.find('name').text
				xmlbox = obj.find('bndbox')
        			b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
				if(cls not in classes or int(difficult) == 1):
					continue



				#bounding = patch_caculate(b,h,w)




				#if((bounding[1]-bounding[0] < 600) or (bounding[3]-bounding[2] < 600)):
					#print("obj_location:%s"%str(b[0])+" "+str(b[1])+" "+str(b[2])+" "+str(3))




				#cut = (img[bounding[2]:bounding[3],bounding[0]:bounding[1],:]).copy()   
				#img.resize((64,64))
				OriginalImgHeight,OriginalImgWidth,OriginalImgChannel = img.shape
				height = OriginalImgHeight / 10
				width = OriginalImgWidth / 10

				print("size:%s"%"h"+str(height)+",w"+str(width))

				img_h,img_w,img_c = img.shape
				print("size:%s"%"h"+str(img_h)+",w"+str(img_w)+",c"+str(img_c))
				#cut = img.resize(height,width)
				cut = cv2.resize(img,(width, height))



				cut_h,cut_w,cut_c = cut.shape
				#print("cut size:%s"%"h"+str(cut_h)+",w"+str(cut_w))
				#print("patch_location>%s"%str(bounding[0])+" "+str(bounding[1])+" "+str(bounding[2])+" "+str(bounding[3]))
				obj_num = 0
				for obj1 in root.iter('object'):
					xmlbox1 = obj1.find('bndbox')
       					difficult1 = obj1.find('difficult').text
        				cls1 = obj1.find('name').text
					bb = (float(xmlbox1.find('xmin').text), float(xmlbox1.find('xmax').text), float(xmlbox1.find('ymin').text), float(xmlbox1.find('ymax').text))
					if(cls1 not in classes or int(difficult1) == 1):
						continue
					obj_num = obj_num  + 1
					bbox=box_resizetune(bb)
					#print("bbox in patch%s"%join([str(a) for a in bbox]))
					#cv2.rectangle(cut,(bbox[0],bbox[2]),(bbox[1],bbox[3]),(255,0,0),2)
					bbox_1=convert((width,height),bbox)
					cls_id1 = classes.index(cls1)
					out_file.write(str(cls_id1) + " " + " ".join([str(a) for a in bbox_1]) + '\n')
				if(obj_num > 0):
					print("save patch %s done"%str(num))
					#print("patch_location>%s"%str(num)+":"+str(bounding[0])+" "+str(bounding[1])+" "+str(bounding[2])+" "+str(bounding[3]))
					cv2.imwrite(imgpath+"%s.jpg"%str(num), cut)#write pitch
					num = num + 1
				else:
					print("no obj in patch")

if __name__ == '__main__':
    filePathC = "insulator(pic)/"
    labelpath = "my_voc/labels/"
    imgpath   = "my_voc/JPEGImages/"
    eachFile(filePathC)
	
