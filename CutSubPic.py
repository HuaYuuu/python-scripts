# -*- coding:utf-8 -*-


# 导入相关的库
from PIL import Image
import os
from os import listdir, getcwd
from os.path import join
import readline
import string





def containVarInString(containVar,stringVar):
    try:
        if isinstance(stringVar, str):
            if stringVar.find(containVar):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)



def find_string(s,t):
    try:
        string.index(s,t)
        return True
    except(ValueError): 
        return False




def cut(source_folder,target_folder,file_path,file_name):
	im =Image.open(file_path)
	txt_obj=file_name+'.jpg.txt'
	print(txt_obj)
	txt_path=os.path.join(source_folder,txt_obj)
	print(txt_path)
	txt_file = open(txt_path,"r")
	n=0
	print(n)
	AllLines=txt_file.readlines()
	print(AllLines)
	for line in AllLines:
		print(line)
		if find_string(line,'insulator1'):
			print("insulator1",containVarInString(line,'insulator1'))
			LableAndLocation = line.split()
			label = LableAndLocation[0]
			left = LableAndLocation[1]
			right = LableAndLocation[2]
			top = LableAndLocation[3]
			bot = LableAndLocation[4]

			x = int(left)
			y = int(top)
			w = int(right)-int(left)
			h = int(bot)-int(top)



			SubPicName = "insulator1/" + file_name + "_insulator1_" + str(n) + ".jpg"

			print(label,left,right,top,bot)
			print(x,y,w,h)


			SubPicPath=os.path.join(target_folder,SubPicName)

			
			#im2 = im.crop((x, y, w, h))
			im2 = im.crop((int(left), int(top), int(right), int(bot)))

			im2.save(SubPicPath)

			n=n+1



		elif find_string(line,'insulator2'):
			print("insulator2",containVarInString(line,'insulator2'))
			LableAndLocation = line.split()

			print(LableAndLocation)

			label = LableAndLocation[0]
			left = LableAndLocation[1]
			right = LableAndLocation[2]
			top = LableAndLocation[3]
			bot = LableAndLocation[4]

			x = int(left)
			y = int(top)
			w = int(right)-int(left)
			h = int(bot)-int(top)



			SubPicName = "insulator2/" + file_name + "_insulator2_" + str(n) + ".jpg"

			print(label,left,right,top,bot)
			print(x,y,w,h)


			SubPicPath=os.path.join(target_folder,SubPicName)

			
			#im2 = im.crop((x, y, w, h))
			im2 = im.crop((int(left), int(top), int(right), int(bot)))

			im2.save(SubPicPath)

			n=n+1


		else:
			print("无目标\n")
		
	print "图片切割成功，切割得到的子图片数为"
	print n
	txt_file.close()


if __name__=="__main__":




	wd = getcwd()
	print(wd)
	source_folder='./uncut_insulator/'#原图片和坐标txt路经
	target_folder='./cutted_insulator/'#提前新建好这个文件夹，文件夹下有两个子文件夹分别命名cable和wire
	file_list=os.listdir(source_folder)
	for file_obj in file_list:                             # 循环读取路径下的文件并筛选输出
		if os.path.splitext(file_obj)[1] == ".jpg":   # 筛选jpg文件
			file_path=os.path.join(source_folder,file_obj) 
			file_name,file_extend=os.path.splitext(file_obj)
			cut(source_folder,target_folder,file_path,file_name)
			print file_obj                           




