import scrapy
class hepsiburada_spider(scrapy.Spider):
    name = "hepsiburada_spider"
    page_count = 0
    product_count = 1
    start_urls = [
         "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?ib=t&siralama=yorumsayisi"
        ]
    root_url = "https://www.hepsiburada.com"
    custom_settings = {"FEEDS":{"results.json":{"format":"json"}}}
    
    def parse(self, response):
        product_title = response.css("div:nth-child(3) a div  div:nth-child(1)  div.p-card-chldrn-cntnr  a  div.prdct-desc-cntnr-wrppr  div.prdct-desc-cntnr div a span::text").extract()
        product_price = response.css("div:nth-child(3) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-aBQpD.fcmrPZ.s3ub8yddjha div.moria-ProductCard-kEwjUF.bmErqM.sz05rlpopwe div a span::text").extract()
        product_score = response.css("div:nth-child(2) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-gkeCQG.fcCI.snsr48kopa5 div a span::text").extract()
        product_comments = response.css("div:nth-child(3) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-gkeCQG.fcCI.snsr48kopa5 div a span::text").extract()
        i = 0
        while (i < len(product_title)):
            self.file.write(str(self.product_count) + ".\n")
            self.file.write("title : " + product_title[i] + "\n")
            self.file.write("price : " + product_price[i] + "\n")
            self.file.write("score : " + product_score[i] + "\n")
            self.file.write("comments : " + product_comments[i] + "\n")
            self.product_count += 1
            i += 1
