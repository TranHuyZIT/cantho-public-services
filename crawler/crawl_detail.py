from selenium import webdriver
class DetailCrawler:
    def __init__(self, url, name, mucdo, linhvuc, coquanthuchien):
        self.url = url
        self.name = name.strip()
        self.mucdo = mucdo.strip()
        self.linhvuc = linhvuc.strip()
        self.coquanthuchien = coquanthuchien.strip()
        self.driver = webdriver.Chrome()
    
    def crawl(self):
        print("Crawling detail", self.name)
    
    
    def persist(self):
        pass
        