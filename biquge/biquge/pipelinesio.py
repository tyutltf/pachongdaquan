import os
print(os.getcwd())


class SixmaoPipeline(object):
    def process_item(self, item, spider):
        #print(item['novel'])

        with open('./data/圣墟.txt', 'a', encoding='utf-8') as fp:
            fp.write(item['novel_neirong'])
            fp.flush()
            fp.close()
        return item
    print('写入文件成功')
