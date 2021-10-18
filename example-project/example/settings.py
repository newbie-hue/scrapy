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

#ȥ�ص���
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#������
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#�������Ƿ�־û��洢
SCHEDULER_PERSIST = True
#���ȶ���
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#����
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#ջ
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    #������ϴ
    'example.pipelines.ExamplePipeline': 300,
    #redis���ݴ��棨�Ƿ������ݿ��е�item���д洢��
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

REDIS_URL = "redis://127.0.0.1:6379"