import os
import sys
def rename_file():

    #(1) get file names form the folder
    file_names = os.listdir(r'D:\MyLearn')
    print file_names
    print(os.getcwd())
    #(2) for each file, rename filename
    os.chdir(r'D:\MyLearn')
    for name in file_names:
        os.rename(name,name.translate(None, "0123456789"))
        print "new name of the file :" + name
    
    
rename_file()
