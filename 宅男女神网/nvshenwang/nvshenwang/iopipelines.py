import time
import requests
import os

class NvshenwangPipeline(object):
    def process_item(self, item, spider):
        print('专辑标题:{0}'.format(item['zhuanjititle']))
        print('图片url:{0}'.format(item['imgurl']))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        imgdir = 'H:/xiezhen/' + item['zhuanjititle']
        print(imgdir)
        if not os.path.exists(imgdir):
            os.mkdir(imgdir)
        for img in item['imgurl']:
            print(img)
            try:
                r = requests.get(img, headers=headers)
                imgfilepath = 'H:/xiezhen/' + item['zhuanjititle'] + '/' + img[-7:]
                with open(imgfilepath, 'wb') as f:
                    f.write(r.content)
            except requests.exceptions.ConnectionError as r:
                r.status_code = "Connection refused"
                time.sleep(5)
        return item