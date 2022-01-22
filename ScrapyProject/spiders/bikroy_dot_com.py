import scrapy

class ScrapeBikroy(scrapy.Spider):
    name = 'bikroy'

    start_urls = [
        'https://bikroy.com/en/ads/bangladesh/mobiles/',
        'https://bikroy.com/en/ads/bangladesh/electronics/',
        'https://bikroy.com/en/ads/bangladesh/home-living/',
        'https://bikroy.com/en/ads/bangladesh/vehicles/',
        'https://bikroy.com/en/ads/bangladesh/property/',
        'https://bikroy.com/en/ads/bangladesh/pets-animals/',
        'https://bikroy.com/en/ads/bangladesh/fashion-beauty/',
        'https://bikroy.com/en/ads/bangladesh/hobbies-sports-kids/',
        'https://bikroy.com/en/ads/bangladesh/business-industry/',
        'https://bikroy.com/en/ads/bangladesh/education/',
        'https://bikroy.com/en/ads/bangladesh/essentials/',
        'https://bikroy.com/en/ads/bangladesh/services/',
        'https://bikroy.com/en/ads/bangladesh/agriculture/'
    ]

    def parse(self, response):

        path_link = response.css('.list-wrapper--t_A02')
        #get_url = response.urljoin(get_path)

        for link in path_link:
            get_path = link.css('.list--3NxGO a::attr(href)').getall()
            for link_1 in get_path:
                post_url = str(link_1)
                get_url = response.urljoin(post_url)


                yield scrapy.Request(get_url, callback=self.parse_content)
            '''meta = {
                'Contents': {
                    'title': response.css('.title-container--1PPnS ::text').extract(),
                    'price': response.css('.price-section--3xCm3 ::text').extract()
                }
            })'''


    def parse_content(self,response):

        title = response.css('.title-container--1PPnS ::text').get()
        price = response.css('.price-section--3xCm3 ::text').get()
        sale_by = response.css('.poster-details--2XBt1 ::text')[0:2].getall()
        others = response.css('.word-break--2nyVq ::text').getall()
        features = response.css('.features--3dZlt p::text').get()
        description = response.css('.description-1nRbz p::text').getall()

        yield {
            'Title': title,
            'Price': price,
            'Owner': sale_by,
            'Specifications': others,
            'Features': features,
            'Description': description
        }



#https://bikroy.com/en/ads/bangladesh?sort=date&order=desc&buy_now=0&urgent=0&page=2 -> all
#https://bikroy.com/en/ads/bangladesh/electronics?sort=date&buy_now=0&urgent=0&page=1
#https://bikroy.com/en/ads/bangladesh/mobiles?sort=date&buy_now=0&urgent=0&page=1