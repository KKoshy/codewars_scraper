

from scrapy import signals


class CodewarsScraperSpiderMiddleware:


    @classmethod
    def from_crawler(cls, crawler):
        """
        Creates the spider
        :param crawler: crawler object
        :return: s
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Processes each response consumed by the spider

        :param response: response object
        :param spider: spider object
        :return: None/Exception
        """
        return None

    def process_spider_output(self, response, result, spider):
        """
        Returns an iterable of the Request or item objects

        :param response: response object
        :param result: result from the spider
        :param spider: spider object
        :return: iterable of request
        """
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        Called when a spider or process_spider_input() method
        (from other spider middleware) raises an exception.

        :param response: response object
        :param exception: exception
        :param spider: spider object
        :return: None/Iterable of request/Item object
        """
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CodewarsScraperDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create the spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
