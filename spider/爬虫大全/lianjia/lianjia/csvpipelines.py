import os
print(os.getcwd())
class LianjiaPipeline(object):
    def process_item(self, item, spider):
        with open('G:\pythonAI\爬虫大全\lianjia\data\house.txt', 'a+', encoding='utf-8') as fp:
            name=str(item['houseinfo'])
            dizhi=str(item['housedizhi'])
            info=str(item['housexiangxi'])
            price=str(item['houseprice'])
            perprice=str(item['houseperprice'])
            fp.write(name + dizhi + info+ price +perprice+ '\n')
            fp.flush()
            fp.close()
        return item

    print('写入文件成功')