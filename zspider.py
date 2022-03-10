import scrapy


class ZspiderSpider(scrapy.Spider):
    name = 'zspider'
    allowed_domains = ['https://soliman4data.wordpress.com/']
    start_urls = ['https://soliman4data.wordpress.com/portfolio']

    def parse(self, response):

        # with the following code we got all data in one cell
        # projects = response.css('strong>a::text').extract()
        # links = response.css('strong>a::attr(href)').extract()

        # If you use 'strong' that means directing to all strong
        # so we got extra 6 empty rows in report.csv
        # rows = response.css('strong')
        
        rows = response.css('p>strong')


        for row in rows:

            projects = row.css('a::text').extract_first()
            links = row.css('a::attr(href)').extract_first()

            yield {
                'projects_names':projects,
                'project_links':links
            }
