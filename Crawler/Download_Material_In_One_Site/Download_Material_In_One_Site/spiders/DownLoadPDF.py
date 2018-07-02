import urllib.request as ul
# ul.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
import scrapy

#!/usr/bin/python
import scrapy

# from scrapy.utils.project import get_project_settings
#
# settings = get_project_settings()


# import sys
# sys.argv = ['scrapy', 'shell', 'http://scrapy.org']
# execute()

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://scis.scichina.com/ssi2018.html',
    ]

    def start_requests(self):
        urls = [
            'http://scis.scichina.com/ssi2018.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.col-sm-12"):
            yield {
                'pdfNum': quote.css("p::attr(id)").extract(),
                'name': quote.css("p a::attr(href)").extract(),
                'text': quote.css("p a::text").extract(),
                # 'link': quote.css('p a::attr(href)'),
                # 'text': quote.css('p a::text'),
                # 'text': quote.css('span.text::text').extract()[0],
                # 'author': quote.css('small.author::text').extract_first(),
                # 'tags': quote.css('div.tags a.tag::text').extract(),
            }

        # next_page = response.css('li.next a::attr(href)').extract()[0]
        # if next_page is not None:
        #     # Method 1
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
            # Method 2
            #response.follow supports relative URLs directly - no need to call urljoin.
            # yield response.follow(next_page, callback=self.parse)


from scrapy.cmdline import execute
execute("scrapy crawl quotes -o quotes.json".split())
