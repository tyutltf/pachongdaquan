from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'jobsspider'])
# execute(['scrapy', 'crawl', 'jobspiders',"-a","start_urls=http://www.baidu.com","-a","args=xxx"])