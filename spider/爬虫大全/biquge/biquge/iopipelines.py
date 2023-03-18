import os
print(os.getcwd())

class BiqugeIoPipeline(object):
    def process_item(self, item, spider):
        #print(item['novel'])
        with open('./biquge/data/留学.txt', 'a', encoding='utf-8') as fp:
            fp.write(item['novel'])
            fp.flush()
            fp.close()
        return item
    print('写入文件成功')