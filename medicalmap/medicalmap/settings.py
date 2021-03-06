# -*- coding: utf-8 -*-

# Scrapy settings for medicalmap project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'medicalmap'

SPIDER_MODULES = ['medicalmap.spiders']
NEWSPIDER_MODULE = 'medicalmap.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'medicalmap (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (compatible;Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'medicalmap.middlewares.MedicalmapSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'medicalmap.middlewares.ProxyMiddleWare': 543,
   'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
   'medicalmap.middlewares.CustomRedirectMiddleWare': 600
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'medicalmap.pipelines.MysqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MONGODB SETTINGS
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 127017
# MONGODB_DB = 'medical_map'
# MONGODB_DOC_HI = 'hospital_info'
# MONGODB_DOC_HD = 'hospital_dep'
# MONGODB_DOC_DI = 'doctor_info'
# MONGODB_DOC_DR = 'doctor_reg_info'

# MYSQL SETTINGS TEST SERVER
MYSQL_HOST = '192.168.99.19'
MYSQL_PORT = 3306
# MYSQL_DB = 'medical_map_update'
MYSQL_DB = 'test'
MYSQL_USER = 'medicalmap1'
MYSQL_PASSWORD = 'medicalmap#1'

# MYSQL SETTINGS LOCALHOST SERVER
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_DB = 'medical_map_update'
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'capricorn1203!'

# DUPEFILTER_DEBUG SETTINGS
DUPEFILTER_DEBUG = True

# RETRY_SETTINGS
RETRY_TIMES = 50  # 默认值为2

# RETRY_HTTP_CODES Default: [500, 502, 503, 504, 408]
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 403, 404, 429]

# HTTPERROR_ALLOWED_CODES：默认为[],[Pass all responses with non-200 status codes contained in this list.]
HTTPERROR_ALLOWED_CODES = [302]

# HTTPERROR_ALLOW_ALL = True  # 默认为false,[Pass all responses, regardless of its status code.]

# Whether the Redirect middleware will be enabled. Default: True
# REDIRECT_ENABLED = False
