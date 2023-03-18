# -*- coding: utf-8 -*-
import scrapy
from ..items import JobspidersItem
count=1

class JobsspiderSpider(scrapy.Spider):
    name = 'jobsspider'
    #allowed_domains = ['search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html']
    #start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html/']
    #start_urls = ['https://search.51job.com/list/010000,000000,0000,01,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']   #北京python
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']      #python
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']        #Java
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,C%252B%252B,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']  #C++
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,PHP,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']           #PHP
    start_urls=['https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']        #北京python
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,web,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']              #web前端
    #start_urls=['https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BC%259A%25E8%25AE%25A1,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']   #会计


    def parse(self, response):
        global count
        currentPageItems = response.xpath('/html/body/div[@class="dw_wp"]/div[@class="dw_table"]/div[@class="el"]')
        print(currentPageItems)
        jobspidersItem = JobspidersItem()
        # currentPageItems = response.xpath('//div[@class="el"]')
        for jobItem in currentPageItems:
            #print('----',jobItem)
            #jobspidersItem = JobspidersItem()

            jobPosition = jobItem.xpath('p[@class="t1 "]/span/a/text()').extract()
            if jobPosition:
                print(jobPosition[0].strip())
                jobspidersItem['jobPosition'] = jobPosition[0].strip()

            jobPositionurl = jobItem.xpath('p[@class="t1 "]/span/a/@href')[0].extract()
            print(jobPositionurl)
            #jobspidersItem['jobPositionhref']=jobPositionurl.strip()

            jobCompany = jobItem.xpath('span[@class="t2"]/a/text()').extract()
            if jobCompany:
                print(jobCompany[0].strip())
                jobspidersItem['jobCompany'] = jobCompany[0].strip()

            jobArea = jobItem.xpath('span[@class="t3"]/text()').extract()
            if jobArea:
                print(jobArea[0].strip())
                jobspidersItem['jobArea'] = jobArea[0].strip()

            jobSale = jobItem.xpath('span[@class="t4"]/text()').extract()
            if jobSale:
                print(jobCompany[0].strip())
                jobspidersItem['jobSale'] = jobSale[0].strip()

            jobDate = jobItem.xpath('span[@class="t5"]/text()').extract()
            if jobDate:
                print(jobCompany[0].strip())
                jobspidersItem['jobDate'] = jobDate[0].strip()


            yield scrapy.Request(url=jobPositionurl, meta={'items': jobspidersItem}, callback=self.positioninfo)

            #yield jobspidersItem  # 通过yield 调用输出管道
            pass
        pass
        if count<1:
            nextPageURL = response.xpath('//li[@class="bk"]/a/@href').extract()  # 取下一页的地址
            print(nextPageURL)
            if nextPageURL:
                #count += 1
                url = response.urljoin(nextPageURL[-1])
                print('下一页url', url)
            # 发送下一页请求并调用parse()函数继续解析
                yield scrapy.Request(url, self.parse, dont_filter=False)
                pass
            else:
                print("退出")
            pass
        else:
            print('完成')

    def positioninfo(self, response):
        jobspidersItem = response.meta['items']
        jobDescribes= response.xpath('/html/body/div[@class="tCompanyPage"]/div[@class="tCompany_center clearfix"]/div[@class="tCompany_main"]/div[@class="tBorderTop_box"]/div[@class="bmsg job_msg inbox"]')
        jobReq = []
        for i in jobDescribes.xpath('p/text()'):
            jobReq.append(i.extract().strip())
        print(jobReq)
        jobspidersItem['jobDescribe'] = str(jobReq)
        yield jobspidersItem





'''
# 斜杠（/）作为路径内部的分割符。
# 同一个节点有绝对路径和相对路径两种写法。
# 绝对路径（absolute path）必须用"/"起首，后面紧跟根节点，比如/step/step/...。
# 相对路径（relative path）则是除了绝对路径以外的其他写法，比如 step/step，也就是不使用"/"起首。
# "."表示当前节点。
# ".."表示当前节点的父节点

nodename（节点名称）：表示选择该节点的所有子节点

# "/"：表示选择根节点

# "//"：表示选择任意位置的某个节点

# "@"： 表示选择某个属性
'''