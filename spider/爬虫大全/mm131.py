import urllib.request
import os

print(os.getcwd())
for i in range(4209, 4461):
    os.mkdir('tupian/' + str(i))
    for j in range(30):
        try:
            url = 'http://img1.mm131.me/pic/' + str(i) + '/' + str(j) + '.jpg'
            print(url)
            # urllib.request.urlretrieve(url, 'lala.jpg')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                'Referer': 'https://www.sogou.com/link?url=DSOYnZeCC_o7btUgpK402wmc9YOcsOr4cOOT57O29F8'
            }
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            with open('tupian/' + str(i) + '/' + str(j) + '.jpg', 'wb') as fp:
                fp.write(response.read())
        except Exception as e:
            print('下载失败，下载下一条')
            break
