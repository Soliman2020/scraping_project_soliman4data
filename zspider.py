import scrapy


class ZspiderSpider(scrapy.Spider):
    
    '''
    Scarping portfolio page to get the project name 
    and its corresponding URL.
    
    '''
    # spider name
    name = 'zspider'
    allowed_domains = ['https://soliman4data.wordpress.com/']
    start_urls = ['https://soliman4data.wordpress.com/portfolio']

    def parse(self, response):

        # with the following code we got all data in one cell
        # projects = response.css('strong>a::text').extract()
        # links = response.css('strong>a::attr(href)').extract()

        rows = response.css('p>strong')

        for row in rows:
            projects = row.css('a::text').extract_first()
            URL = row.css('a::attr(href)').extract_first()

            yield {
                'projects_names':projects,
                'project_links':URL
            }
