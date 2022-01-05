import scrapy
class trendyol_spider(scrapy.Spider):
    name = "trendyol_spider"
    product_count = 1
    start_urls = [
         "https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1"
        ]
    root_url = "https://www.trendyol.com"
    custom_settings = {"FEEDS":{"results.json":{"format":"json"}}}
    
    def parse(self, response):
        product_title = response.css("div.srch-rslt-cntnt div.srch-prdcts-cntnr div:nth-child(3) div div:nth-child(1) div.p-card-chldrn-cntnr a div.prdct-desc-cntnr-wrppr div.prdct-desc-cntnr div span.prdct-desc-cntnr-name.hasRatings::text").extract()
        product_price = response.css("div div.srch-rslt-cntnt div.srch-prdcts-cntnr div:nth-child(3) div div:nth-child(1) div.p-card-chldrn-cntnr a div.prdct-desc-cntnr-wrppr div.price-promotion-container div.prc-cntnr div").extract()
        product_score = response.css("div div.srch-rslt-cntnt div.srch-prdcts-cntnr div:nth-child(3) div div:nth-child(1) div.p-card-chldrn-cntnr a div.prdct-desc-cntnr-wrppr div.ratings span::text").extract()
        #product_comments = response.css("5 div a span::text").extract()
        i = 0
        while (i < len(product_title)):
            self.file.write(str(self.product_count) + ".\n")
            self.file.write("title : " + product_title[i] + "\n")
            self.file.write("price : " + product_price[i] + "\n")
            self.file.write("score : " + product_score[i] + "\n")
            #self.file.write("comments : " + product_comments[i] + "\n")
            self.product_count += 1
            i += 1
