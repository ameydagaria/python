import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
class FirstSpider(scrapy.Spider):
	name = "tripadvisor"
	allowed_domains = ["tripadvisor.in"]
	start_urls = ["https://www.tripadvisor.in/Restaurants-g297654-Pune_Maharashtra.html"]
		

	def parse(self,response):
		urls = response.xpath('//h3[@class="title"]/a/@href').extract()
		for url in urls:
			absolute_url = response.urljoin(url)
			#yield {'Url': absolute_url}
			yield scrapy.Request(absolute_url,
								callback=self.parse_restaurant)
		next_page_url = response.xpath('//a[text()="Next"]/@href').extract_first()
		next_absolute_url = response.urljoin(next_page_url)
		yield scrapy.Request(next_absolute_url,callback=self.parse)


	def parse_restaurant(self, response):
		rating = response.xpath('//img[@property="ratingValue"]/@content').extract_first()
		name = response.xpath('//div[@class="mapContainer"]/@data-name').extract_first()
		latitude = response.xpath('//div[@class="mapContainer"]/@data-lat').extract_first()
		longitude = response.xpath('//div[@class="mapContainer"]/@data-lng').extract_first()
		url = response.url
		yield {'Rating': rating,
				'Name':name,
				'latitude':latitude,
				'longitude':longitude,
				'url':url}
