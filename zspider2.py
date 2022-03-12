import scrapy


class Zspider2Spider(scrapy.Spider):
    ''' 
    Start from a page and get URLs of other pages
    that I want to apply scrapy on them.
    '''
    # new spider name
    name = 'zspider2'
    allowed_domains = ['soliman4data.wordpress.com']
    start_urls = ['https://soliman4data.wordpress.com/portfolio/']

    def parse(self, response):
        # direct the spider to the parent container
        rows = response.css('p>strong')
        # doing for loop to take each output alone
        for row in rows:
            URL = row.xpath('./a/@href').extract_first()
            # forward scraped urls to another parser to get extra data
            yield response.follow(url=URL , callback = self.parse2)

    def parse2(self, response):

        githubs_link = response.xpath('//div[@class="wp-block-button"]/a/@href').extract_first()
        
        # getting text was tricky because of each page diff. format
        # using //text instead of /text to get all text inside the header
        title = response.xpath('//div[@class="entry-content"]/h2[1]//text()').extract()

        yield {
            'github_link':githubs_link,
            'page_title':title    
        }
        
        # Note that: outputs are 4 not 5 because not all pages have github links.
