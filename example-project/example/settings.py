# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#去重的类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#调度器是否持久化存储
SCHEDULER_PERSIST = True
#优先队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#栈
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    #数据清洗
    'example.pipelines.ExamplePipeline': 300,
    #redis数据储存（是否在数据库中的item进行存储）
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

REDIS_URL = "redis://127.0.0.1:6379"