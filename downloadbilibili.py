import os
n=int(input("视频的数量：")) #视频的数量
s=input("视频的链接，不要最后一个数字：") #视频的链接
for i in range(1, n+1):
    cmd= 'annie'+' '+'https://www.bilibili.com/video/'+s+str(i)
    os.system(cmd)
    print("完成第{0}个视频\n".format(i))
