# scrapy
scrapy/scrapy_redis...


'''


1、scrapy_spider
    腾信视频的实现了           多线程、日志  等基本的使用方式
    糗事百科实现了             1、持久化存储
                                    mysql/mongdb/本地
                                    数据的清洗  re.sub()   \ .strip()   \"".join()  lambda  strip()  join()
                                            import re
                                            ex_list = ['\3','\3',' ','mklmlkm']
                                            a = filter(lambda x:re.sub("\3",'',x).strip(),ex_list)
                                            print("".join(list(a)))

                            2、随机的ua
                                    request.headers["User_Agent"] = ''
                            3、代理
                                    request.meta['proxy'] = ''
                            4、cookies的登录：（cookie放到headers中不能自己构造的cookie,但是可以使用settings中的cookies）
                                        request(cookies放入headers,cookies作为参数、session、selenium)
                                        1、start_request中的yield scrapy.Request(......cookies=cookies)  //COOKIES_ENABLED = True
                                        2、headers  settings中的设置
                            5、post请求
                                        1、源码网页中有form表单，那么可以在scrapy.FormRequest.form_response(.....formdata={账号的name标签：账号。密码的name标签：密码})   不常用
                                        2、直接构造表单。post_data   在scrapy.FormRequest(.....formdata=post_data)
                                        3、scrapy.Request(url,method = 'POST',body=post_data)
                            6、爬虫的去重  （在当前的爬虫会进行屈从）
                                  打开了一个恩建

2、crawlspider  的使用
    创建
        circ文件的
        scrapy startproject 项目名
        cd 项目名
        scrapy genspider -t crawl 爬虫名 域名



    CrawlSpider  circ因为网站的关闭，现在呈现的为逻辑


    rule 链接提取器(会自动的补全不完整的href)  （正则或者xpath提取）
            allow（正则）满足的被抓取
            deny(正则 ) 满足的不被抓取
            allow_domains:响应会被提取的域名
            deny_domains:不会被提取的域名
            restrict_xpaths:和allow共同作用，满足的会被提取


        callback
            这个链接的解析函数
        folow 默认为False
            提取之后的链接进行请求，是否还进行同样的提取
        process_links:
            指定该spider中的哪个函数会被调用，从link_extractor中获取到链接列表的时候会调用该函数（只要用来过滤url和去重）
        process_request:
            指定该spider中的哪个函数会被调用，该规则提取到每个request的时候都会调用该函数。(用来过滤resuest)

    注意点：
        通过 -t crawl进行创建
        不能重写paser函数




3、异步的协程框架注意点：suning_book
    1、内存共享问题    在爬取suning_book的时候，有大分类、小分类、页面详情    在传递item的时候  因为是异步的框架前面的会改变item里面的内容，
                    其实也就是说item传递的是spider中对应的内容   但是被改变了  如果想实现对应，那么就将其进行deepcopy
    2、js生成的问题   通过js解决


4、scrapy_redis
        强大的地方    1、request去重  帮助持久化的去重   实现增量式爬虫
                    2、爬虫持久化
                    3、轻松实现分布式
                    4、断点续爬？
        redis的复习
                cd  进入redis
                redis-server stop  ------>redis停止
                redis-server.exe redis.windows.conf   --->开启
                cmd  redis-cli  (本机)进入
                    redis-cli -h<hostname> -p<port> 远程连接


                list
                    lpush key value  左边添加
                    lrange key start stop 返回所有值
                    llen key   返回长度
                set
                    sadd  key value   set添加数据
                    smembers  key  获取所有数据
                    scard  key 获取长度
                zset
                    zadd key score value  添加
                    zrange  key start stop (withscores)获取元素
                    zcard  key

                清空数据库   flushdb
        scrapy_redis
            setting
                    REDIS_URL = "redis://127.0.0.1:6379"
                    or
                    REDIS_HOST = '127.0.0.1'
                    REDIS_PORT = '6379'
            源码解读（scrapy_redis）
                piplines  进行持久化储存的地方 _process_item
                dupefilter  通过request特征去重生成指纹
                                默认通过sha1 request.method\request.url\request.body or b''\(include_headers)
                                request_fingerprint
                scheduler
                        close方法   如果不持久化存储的话，爬虫停止时就清空指纹等内容
                        enqueue_request方法  如果not request.dont_filter and self.df.request_seen(request) 就不如队列
                                            否则就 进入队列
                                            或者  在Request对象中设置   dont_filter  = True ，那么就不会请求去重（用于更新）
                                            和scrapy的相同   url在start_url的时候，不管之前是否存在，都会入队。
                        使用sadd添加指纹 根据返回值来判断是否入队。

        可以由scrapy改造而来
            加上

                #去重的类
                DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
                #调度器
                SCHEDULER = "scrapy_redis.scheduler.Scheduler"
                #调度器是否持久化存储
                SCHEDULER_PERSIST = True

                ITEM_PIPELINES = {
                    #数据清洗
                    'example.pipelines.ExamplePipeline': 300,
                    #redis数据储存（是否在数据库中的item进行存储）
                    'scrapy_redis.pipelines.RedisPipeline': 400,
                }
                REDIS_URL = "redis://127.0.0.1:6379"


5、分布式爬虫
        1、spider
            1、allowed_domains  的问题。因为是从scrapy中建立起来的，所以就没有
                def __init__(self)
                pass
                的初始化方法
                而是使用allowed_domains来进行使用。
            2、spider继承的类是RedisSoider,所以
                1、from scrapy_redis.spider import RedisSpider
                2、将继承的类更改为   RedisSpider
            3、start_url储存在redis中，所以
                把start_url 更改为
                redis_key = 'dangdang'  （读取这个键里面的url作为起始的url）
            4、在redis中插入  起始的url 对应的键值对  ----以列表的形式  lpush
            5、加入scrapy_redis中 setting 添加的内容
            6、更换rREDIS_URL 为本机的真实IP
        2、crawlspider
            1、继承的父类是RedisCrawlSpider




1、断点续爬的实现原理
2、增量爬虫的实现原理



'''