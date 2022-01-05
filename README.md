# 
<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="etc\logo.jpg" alt="Logo">
  </a>

<h2 align="center"><strong>erencomp - a web crawling app</strong></h2>

  <div align="center">
    For our project we decided to create a web-based app to make our users find ease in the process of buying a computer. Choosing a new computer is a big decision, so with our app you’ll be able to enter your desired features and we will gather data from all across the web for you to select the seller you wish to buy your computer from. The filters available will be the price and other users’ reaction to the product, such as score or the amount of comments it has gotten.
    <br />
  </div>
</div>

# About The Project

We made this project with the help of the Scrapy official documentation.

First we created a template crawler project with the scrapy startproject command, then we added our spiders.

A brief explanation of how they work:

  - We aimed to pull the data from two shopping sites for starter: Trendyol and HepsiBurada. We created two spider files accordingly.
  - A spider essentially is a class you define Scrapy uses that class to crawl through websites according to your wishes. Inside this class, first part of teh code consists of sending requests to a certain site, and the second part is getting the response and breaking down the received data to get to what we need.

1. Getting a Response
As the example from our HepsiBurada spider presents below, this first part is for getting the requests.  We pick the starting url and send requests to it. 
```sh
  import scrapy
  class hepsiburada_spider(scrapy.Spider):
      name = "hepsiburada_spider"
      product_count = 1
      start_urls = [
          "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?ib=t&siralama=yorumsayisi"
          ]
      root_url = "https://www.hepsiburada.com"
```
This little part ensures that out final outputs are written to a json rather than the default txt.
```sh
  custom_settings = {"FEEDS":{"results.json":{"format":"json"}}}
```
Now we just need to parse the responses. We used the CSS selector method to reach the elements we needed.
```sh    
  def parse(self, response):
      product_title = response.css("div:nth-child(3) a div  div:nth-child(1)  div.p-card-chldrn-cntnr  a  div.prdct-desc-cntnr-wrppr  div.prdct-desc-cntnr div a span::text").extract()
      product_price = response.css("div:nth-child(3) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-aBQpD.fcmrPZ.s3ub8yddjha div.moria-ProductCard-kEwjUF.bmErqM.sz05rlpopwe div a span::text").extract()
      product_score = response.css("div:nth-child(2) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-gkeCQG.fcCI.snsr48kopa5 div a span::text").extract()
      product_comments = response.css("div:nth-child(3) a div.moria-ProductCard-fHiOwt.fAtrjo.sz6fy89k1sx div.moria-ProductCard-gkeCQG.fcCI.snsr48kopa5 div a span::text").extract()
```
All we need to do now is to write the extracted elements to a json file under the while loop. This loop ensures that program continues as much as there are products.
```sh 
  i = 0
  while (i < len(product_title)):
      self.file.write(str(self.product_count) + ".\n")
      self.file.write("title : " + product_title[i] + "\n")
      self.file.write("price : " + product_price[i] + "\n")
      self.file.write("score : " + product_score[i] + "\n")
      self.file.write("comments : " + product_comments[i] + "\n")
      self.product_count += 1
      i += 1
```
