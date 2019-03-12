# coding=utf-8
import os
def rename(): 
    path="/home/liyi/yolov3/YOLOTrain/Boat/V2_NIMIZI_2/view3" #文件路径
    Newpath="/home/liyi/yolov3/YOLOTrain/label"
    filelist = os.listdir(path) #该文件夹下的所有文件
    count =416

    for file in filelist: #遍历所有文件 包括文件夹
	if file.endswith('.txt'):        
		Olddir = os.path.join(path,file)#原来文件夹的路径
		if os.path.isdir(Olddir):#如果是文件夹，则跳过
			continue
		filename = os.path.splitext(file)[0]  #文件名
		filetype = ".txt"#os.path.splitext(file)[1]   文件扩展名
		Newdir = os.path.join(Newpath,str(count)+filetype) #新的文件路径
		os.rename(Olddir,Newdir) #重命名
		count += 1
rename()
