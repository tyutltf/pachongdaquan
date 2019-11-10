print('正在爬取...')
class MeizituPipeline(object):
    def process_item(self, item, spider):
        print('标签名称:',item['tag_name'])
        print('标签链接:',item['tag_href'])
        print('页码:',item['page_list'])
        print('图片专辑名称:',item['album_name'])
        print('图片专辑链接:',item['album_href'])
        print('照片标题:',item['img_title'])
        print('照片链接:',item['img_src'])
        print('照片链接集合:',item['img_urls'])
        print('----------------')
        return item
