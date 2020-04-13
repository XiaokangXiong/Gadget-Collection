import os
path = "D:/xiaokang" #目标文件夹
files= os.listdir(path) #得到文件夹下的所有文件名称
m=0
n=1
for file in files: #遍历文件
     old=path+os.sep+files[m]
     x=str(n)
     x=x.zfill(4)
     new=path+os.sep+x+'.png'
     os.rename(old,new)
     m+=1
     n+=1   
