import webbrowser
import time
import pdb
import os

break_counter = 0
total_times = 3
print "This program started on :" + time.ctime()
print os.sep
print os.name
print os.getcwd()
path = 'D:/game/gtav/bin/gtav.exe'
print os.path.split(path)[0]
print os.path.split(path)[1]
print os.path.isfile(path)
path = 'D:\\hadoop-2.6.5\\bin'
print(os.path.exists(path))
path = 'D:\\hadoop-2.6.5\\bin\\hadoop'
print(os.path.exists(path))
path = 'D:/test/sdf\zfb'
print(os.path.normpath(path))

pdb.set_trace()
while(break_counter < total_times ):
    print os.listdir(os.getcwd())
    time.sleep(5)
    webbrowser.open("https://www.baidu.com/")
    break_counter = break_counter +1
    
print "Good bye"
