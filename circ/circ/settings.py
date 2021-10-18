# Scrapy settings for circ project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'circ'

SPIDER_MODULES = ['circ.spiders']
NEWSPIDER_MODULE = 'circ.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'circ (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh,zh-CN;q=0.9',
  'Referer':'https://tieba.baidu.com/',
  'Host': 'tieba.baidu.com',
  'Cookie': 'bdshare_firstime=1625363488242; BIDUPSID=5AD394E107102A345FE4A04D8110F605; PSTM=1630709754; BDUSS=5YSVZka0VjU3hFWURubHR6cGl6UzczZVNMNEdXSmhQbFVhQlpXdlZ4bUo2MXRoSVFBQUFBJCQAAAAAAAAAAAEAAAA7TBwjzt7EztDHv9XCqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIleNGGJXjRhZ3; BDUSS_BFESS=5YSVZka0VjU3hFWURubHR6cGl6UzczZVNMNEdXSmhQbFVhQlpXdlZ4bUo2MXRoSVFBQUFBJCQAAAAAAAAAAAEAAAA7TBwjzt7EztDHv9XCqQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIleNGGJXjRhZ3; __yjs_duid=1_f7d41056c7881d2ffa3cb9688ec9eeb41630842971104; STOKEN=2b282e41ba7ffe0f6097dfd5f18388bf3ac72746276e6f783ece9db4bf6443ee; BAIDUID=CCD79A86B3C1CB66DDF532219C74C48E:FG=1; BDSFRCVID=VXLOJeCmHxxnrKRHV9vSbVa1n2KK0gOTHllnPYmRkagtD-PVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJkD_I_hJKt3e-5P-J3ObICShfbL5-3XHD7yWCvCypRcOR5Jhf7W2-CXyn57LjcqLKrp3Cj8tqvvhb3O3M7Sh-CrWfcNa-oMbgPLbUQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_J6-DtJ6P; BCLID_BFESS=9690485904643966353; BDSFRCVID_BFESS=VXLOJeCmHxxnrKRHV9vSbVa1n2KK0gOTHllnPYmRkagtD-PVJeC6EG0Ptf8g0KubFTPRogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJkD_I_hJKt3e-5P-J3ObICShfbL5-3XHD7yWCvCypRcOR5Jhf7W2-CXyn57LjcqLKrp3Cj8tqvvhb3O3M7Sh-CrWfcNa-oMbgPLbUQF5l8-sq0x0bOte-bQypoa0q3TLDOMahkM5h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjISKx-_J6-DtJ6P; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34653_34530_34067_31253_34711_34584_34505_34708_34813_26350_34760_34627_34426_34473_34679; BA_HECTOR=a42hak2gal8k04a5rj1gme3qp0r; delPer=0; PSINO=7; BAIDUID_BFESS=CCD79A86B3C1CB66DDF532219C74C48E:FG=1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1632246343,1633404715,1633457383,1634144278; st_key_id=17; wise_device=0; BAIDU_WISE_UID=wapp_1634144284882_977; USER_JUMP=-1; video_bubble589057083=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1634146070; ab_sr=1.0.1_MjY1NzkwNmUxOGYyYWVjMGViY2Q4M2VkMmZjNWU5ZGUyNzE3Y2I5MDZhNjBiNGMxMTYyMjc1YjQ3ZjZhODYwOWJjMWY0YWEyNjljMGRkNDg1Nzg0NDhiZGJjMmM1MDFjMjhhMjNhNjUwMTUwYmQwZTU3ZTkyYTM5YWQ4ZjNiNzg4MjVmMTcyMWZlMzc4YjhkMDY0ZTA5NzY0NzU4YWQ5Mjg4NjQ0ZGNhY2VhMzY2MGJlYjE5NzYwMDEwMWMzMmE4; st_data=3e1513253923f5642f3e1558df6e7e979950ae26324a976f20d3701a96075fc8dba8be5eb03d5a2dc9320ea264fe3c19f7f1afa2ac6242ffd970fd91553807f967faf95c025f4f904a3c681527b236436899135e5c823d9bab7aa3648ce983181a98c746f4813f4216a77cc3834261fcdc8e7a1b267c42a0f5861ff187181d07; st_sign=ba6ab9d4',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'circ.middlewares.CircSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'circ.middlewares.CircDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'circ.pipelines.CircPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
