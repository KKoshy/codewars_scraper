"""
Scrapy settings for codewars_scraper project

"""

BOT_NAME = 'codewars_scraper'

SPIDER_MODULES = ['codewars_scraper.spiders']
NEWSPIDER_MODULE = 'codewars_scraper.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

