# -*- coding: utf-8 -*-
import os
 
def delete_file_by_txt(dirname,txt_file_path):
	filelist = os.listdir(dirname)
	count = 1
	for file in filelist:
		txtfile = open(txt_file_path,'r')
		oldpath = os.path.join(dirname,file)
		filename = os.path.splitext(file)[0]#文件名
		filetype = os.path.splitext(file)[1]#文件类型
		for txtline in txtfile:
			if(txtline.strip()==file.strip()):
				my_file = dirname + file.strip()
				if os.path.exists(my_file):
					os.remove(my_file)
					print('delete file:%s'%my_file)
				else:
					print('no such file:%s'%my_file)
				print(count)
				count = count + 1

delete_file_by_txt("./JPEGImages_del/","DeletePic.txt")
