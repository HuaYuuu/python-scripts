import os
from os import listdir, getcwd
from os.path import join

if __name__ == '__main__':
    wd = getcwd()
    source_folder='./NEST_new/'
    dest='train_new.txt' 
    #dest2='val_test.txt'  
    file_list=os.listdir(source_folder)       
    train_file=open(dest,'w')                 
    #val_file=open(dest2,'w')                  
    for file_obj in file_list:                
        file_path=os.path.join(source_folder,file_obj) 
        file_name,file_extend=os.path.splitext(file_obj)
        #file_num=int(file_name)
	train_file.write('%s/NEST_new/%s.jpg\n'%(wd, file_name)) 
	#train_file.write('%s\n'%(file_name)) 
        #if(file_num>300 and file_num<300):                     
        #    val_file.write('%s/high_voltage/%s.jpg\n'%(wd, file_name)) 
        #else :
        #    train_file.write('%s/high_voltage/%s.jpg\n'%(wd, file_name))    
    train_file.close()
    #val_file.close()
