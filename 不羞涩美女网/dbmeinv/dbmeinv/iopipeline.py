import requests
import time

class DbmeinvIoPipeline(object):
    # def process_item(self, item, spider):
    #     print('图片标题:{0}'.format(item['imgname']))
    #     print('图片url:{0}'.format(item['imgurl']))
    #     return item

    def process_item(self,item,spider):
        print('图片标题:{0}'.format(item['imgname']))
        print('图片url:{0}'.format(item['imgurl']))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        r = requests.get(item['imgurl'], headers=headers)
        imgfilepath = 'G:/meinvtupian/' + item['imgurl'][-20:]
        with open(imgfilepath, 'wb') as f:
            f.write(r.content)
        print('正在保存图片：', item['imgname'])
        time.sleep(0.1)

        return item
