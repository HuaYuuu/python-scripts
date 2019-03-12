import os
from os import listdir, getcwd
from os.path import join
import numpy as np
from xml.dom.minidom import Document

classe_my = ['ship','warship']

def loc_caculate(x,y,w,h,size_w,size_h):
		x_1 = x*size_w
		y_1 = y*size_h
		w_1 = w*size_w
		h_1 = h*size_h
		#print(x_1,y_1,w_1,h_1)
		x_min = int(x_1-w_1/2)
		x_max = int(x_1+w_1/2)
		y_min = int(y_1-h_1/2)
		y_max = int(y_1+h_1/2)
		return (x_min,x_max,y_min,y_max)
		
def writeInfoToXml(arry, filename):
        doc = Document()
        orderlist = doc.createElement('annotation')
        doc.appendChild(orderlist)
	r,c = data_array.shape

	size = doc.createElement('size')
        orderlist.appendChild(size)
	width = doc.createElement('width')
	widthtxt = doc.createTextNode(str(600))
	width.appendChild(widthtxt)
	size.appendChild(width)

	height = doc.createElement('height')
	heighttxt = doc.createTextNode(str(600))
	height.appendChild(heighttxt)
	size.appendChild(height)

	depth = doc.createElement('depth')
	depthtxt = doc.createTextNode(str(3))
	depth.appendChild(depthtxt)
	size.appendChild(depth)

	for i in range(r):
		#print(i)
		(classes, p_x, p_y, p_w,p_h) = (arry[i][0], arry[i][1], arry[i][2], arry[i][3],arry[i][4])
		#print(arry[i][0], arry[i][1], arry[i][2], arry[i][3],arry[i][4])
		b = loc_caculate(p_x, p_y, p_w,p_h,600,600)
           	#print(b)
		obj = doc.createElement('object')
           	orderlist.appendChild(obj)
	    
           	name = doc.createElement('name')
           	nametext = doc.createTextNode(classe_my[int(classes)])
           	name.appendChild(nametext)
            	obj.appendChild(name)

           	pose = doc.createElement('pose')
           	posetext = doc.createTextNode('Unspecified')
           	pose.appendChild(posetext)
            	obj.appendChild(pose)

           	difficult = doc.createElement('difficult')
           	difficulttext = doc.createTextNode(str(0))
           	difficult.appendChild(difficulttext)
           	obj.appendChild(difficult)
		

            	bndbox = doc.createElement('bndbox')
 	    	obj.appendChild(bndbox)
	    
	    	xmin = doc.createElement('xmin')
	   	xmintxt = doc.createTextNode(str(b[0]))
	   	xmin.appendChild(xmintxt)
	   	bndbox.appendChild(xmin)

	    	ymin = doc.createElement('ymin')
	   	ymintxt = doc.createTextNode(str(b[2]))
	   	ymin.appendChild(ymintxt)
	   	bndbox.appendChild(ymin)

	    	xmax = doc.createElement('xmax')
	   	xmaxtxt = doc.createTextNode(str(b[1]))
	   	xmax.appendChild(xmaxtxt)
	   	bndbox.appendChild(xmax)

	    	ymax = doc.createElement('ymax')
	   	ymaxtxt = doc.createTextNode(str(b[3]))
	   	ymax.appendChild(ymaxtxt)
	   	bndbox.appendChild(ymax)
		
       
        with open(filename, 'w') as f:
            f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))
        return

def arryfromtxt(txtfile):
	f = open(txtfile)
	line = f.readline()
	data_list = []
	while line:
    		num = list(map(float,line.split()))
   	 	data_list.append(num)
    		line = f.readline()
	f.close()
	data_array = np.array(data_list)
	return data_array

if __name__ == '__main__':
	wd = getcwd()
	source_folder_name='/my_voc_4k/JPEGImages/'
	target_folder_name='/my_voc_4k/labels/'
	source_folder='./my_voc_4k/JPEGImages/'
	target_folder='./my_voc_4k/labels/'
	dest='train_4k.txt' 
	dest2='val_4k.txt'  
	file_list=os.listdir(source_folder)       
	train_file=open(dest,'w')                 
	val_file=open(dest2,'w')                  
	for file_obj in file_list:                
		file_path=os.path.join(source_folder,file_obj) 
		file_name,file_extend=os.path.splitext(file_obj)
		file_num=int(file_name)
		if(file_num>300 and file_num<600):                     
			val_file.write('%s%s%s.jpg\n'%(wd, source_folder_name, file_name)) 
		else :
			train_file.write('%s%s%s.jpg\n'%(wd, source_folder_name, file_name))   
		data_array = arryfromtxt('%s%s.txt'%(target_folder,file_name))
		writeInfoToXml(data_array,'%s%s.xml'%(target_folder,file_name)) 
	train_file.close()
	val_file.close()
	
	
