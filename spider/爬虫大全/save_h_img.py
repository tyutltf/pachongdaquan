import time
import requests
import os


def saveImage(imgname,imgurl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    r = requests.get(imgurl,headers=headers)
    imgfilepath='G:/htupian/'+imgname+'/'+imgurl[-8:]
    print(imgfilepath)
    imgdir='G:/htupian/'+imgname
    print(imgdir)
    if not os.path.exists(imgdir):
        print("不存在")
        os.mkdir(imgdir)

    with open(imgfilepath, 'wb') as f:
        f.write(r.content)
    print('正在保存图片：', imgname)
    time.sleep(0.1)


imgurlfile='G:\pythonAI\爬虫大全\htupian\htupian1.txt'
with open(imgurlfile,'r',encoding='utf-8')as file:
    lines=file.readlines()
    for line in lines:
        list1=line.split(',')
        imgname=list1[0]
        imgurl=list1[1][:-1]
        print(imgname,imgurl)
        saveImage(imgname,imgurl)



