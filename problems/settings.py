# Scrapy settings for problems project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'problems'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['problems.spiders']
NEWSPIDER_MODULE = 'problems.spiders'
DEFAULT_ITEM_CLASS = 'problems.items.ProblemsItem'
USER_AGENT = '%s/%s' % (BOT_NAME,BOT_VERSION)
ITEM_PIPELINES = [
    'problems.pipelines.ProblemsPipeline',
    ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'problems (+http://www.yourdomain.com)'
