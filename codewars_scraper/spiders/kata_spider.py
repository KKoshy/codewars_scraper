"""
Spider to crawl codewars.com site

"""

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://www.codewars.com'
NEXT_PAGE_URL = 'https://www.codewars.com/kata/search/?q=&beta=false&page={}'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


class KataSpider(scrapy.Spider):
    name = 'kata'
    start_urls = ['https://www.codewars.com/kata/search/?q=&beta=false']

    def parse(self, response, **kwargs):
        for kata in response.xpath("//div[contains(@class, 'list-item-kata')]"):
            yield response.follow(BASE_URL + kata.css("a.ml-2::attr(href)").get(), callback=self.parse_kata)

        page_no = response.css('div.js-infinite-marker::attr(data-page)').get()
        if page_no is not None:
            next_page = NEXT_PAGE_URL.format(page_no)
            yield response.follow(next_page, callback=self.parse)

    def parse_kata(self, response):
        stats_data = {'name': response.css("div h4.ml-2::text").get(),
                      'rank': response.css("div.inner-small-hex span::text").get().replace(' kyu', '')}
        driver.get(response.url)

        stats_criteria = driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
        stats_criteria = [criteria.text for criteria in stats_criteria]
        stats_value = driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
        stats_value = [value.text for value in stats_value]
        yield {**stats_data, **dict(zip(stats_criteria, stats_value))}
