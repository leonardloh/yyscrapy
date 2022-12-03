from distutils.command.clean import clean
import scrapy


def clean_price_str(in_str):
    return in_str.replace('\n', '').replace(' ','')

class YueYuSpider(scrapy.Spider):
    name = 'yueyu'
    start_urls = [
        'https://yesnatural.my/collections/%E4%BF%9D%E5%81%A5%E5%93%81-%E5%85%BB%E7%94%9F-%E9%85%B5%E7%B4%A0-supplement-health-enzyme',
        'https://yesnatural.my/collections/%E4%BC%91%E9%97%B2%E9%9B%B6%E9%A3%9F-health-snacks',
        'https://yesnatural.my/collections/%E5%81%A5%E5%BA%B7%E6%A4%8D%E7%89%A9%E6%B2%B9-health-plant-oil',
        'https://yesnatural.my/collections/%E9%A5%AE%E6%96%99-%E8%8C%B6-%E5%92%96%E5%95%A1',
        'https://yesnatural.my/collections/%E5%A4%A9%E7%84%B6%E5%8D%B3%E9%A3%9F%E9%9D%A2-%E7%B2%A5-natural-noodles-porridge',
        'https://yesnatural.my/collections/%E5%B9%B2%E8%B4%A7-%E7%B4%A0%E6%96%99',
        'https://yesnatural.my/collections/%E8%B0%83%E5%91%B3-%E9%85%B1%E6%96%99-seasoning-sauce',
        'https://yesnatural.my/collections/%E6%8A%B9%E9%85%B1-%E6%9E%9C%E9%85%B1',
        'https://yesnatural.my/collections/dried-herbs',
        'https://yesnatural.my/collections/%E6%97%A5%E5%B8%B8%E7%94%A8%E5%93%81-%E6%B8%85%E6%B4%81%E7%94%A8%E5%93%81-daily-necessities-cleaning-supplies',
        'https://yesnatural.my/collections/gardening',
        'https://yesnatural.my/collections/%E9%85%A5%E6%B2%B9%E7%81%AF'
        ]

    def parse(self, response):
        images = response.css('img.product__img').xpath('@src').extract()
        for i, products in enumerate(response.css('div.wide--one-fifth')):
            scrapped_prices = products.css('p.grid-link__meta::text').getall()
            filtered_empty_scrapped_prices = (clean_price_str(p) for p in scrapped_prices if len(clean_price_str(p)) > 0)
            yield {
                'collection': response.css("h1.section-header__title::text").get().encode('utf-8'),
                'name': products.css('p.grid-link__title::text').get().encode('utf-8'),
                'price': next(filtered_empty_scrapped_prices),
                'img': images[i]
            }

        next_page = response.xpath("//a[@title='Next »']/@href").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)