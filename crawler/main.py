import bs4
import multiprocessing
from selenium import webdriver
from crawl_detail import DetailCrawler
import os
from crawl_dichvucong import CrawlNhomDichVuCong
page = 1

def get_url():
    print("Getting url for page", page)
    return f"https://dichvucong.cantho.gov.vn/dich-vu-cong-truc-tuyen?p_p_id=thutuchanhchinh_WAR_uniportalportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_thutuchanhchinh_WAR_uniportalportlet_loaiDichVuBuuDien=-1&_thutuchanhchinh_WAR_uniportalportlet_mucDo=0&_thutuchanhchinh_WAR_uniportalportlet_tenThuTuc=&_thutuchanhchinh_WAR_uniportalportlet_iddonvi=0&_thutuchanhchinh_WAR_uniportalportlet_idCoQuan=0&_thutuchanhchinh_WAR_uniportalportlet_maLinhVuc=&_thutuchanhchinh_WAR_uniportalportlet_capThucHien=-1&_thutuchanhchinh_WAR_uniportalportlet_nhomId=0&_thutuchanhchinh_WAR_uniportalportlet_delta=20&_thutuchanhchinh_WAR_uniportalportlet_keywords=&_thutuchanhchinh_WAR_uniportalportlet_advancedSearch=false&_thutuchanhchinh_WAR_uniportalportlet_andOperator=true&_thutuchanhchinh_WAR_uniportalportlet_resetCur=false&_thutuchanhchinh_WAR_uniportalportlet_cur={page}"


NUMBER_OF_PROCESSES = 4
def worker(url, name, mucdo, linhvuc, coquanthuchien):
    detail_crawler = DetailCrawler(url, name, mucdo, linhvuc, coquanthuchien)
    detail_crawler.crawl()

def create_drop_data():
    for file in os.listdir("./data/thutuchanhchinh"):
        os.remove(os.path.join("./data/thutuchanhchinh", file))

    os.removedirs("./data/thutuchanhchinh")
    os.makedirs("./data/thutuchanhchinh")

def main():
    create_drop_data()
    while True:
        driver = webdriver.Chrome()
        driver.get(get_url())
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")
        table_body = soup.find("tbody", {"class": "table-data"})
        if not table_body:
            print("Completed at page", page)
            break
        table_rows = table_body.find_all("tr")
        for row in table_rows:
            cells = row.find_all("td")
            a_element = cells[1].find("a")
            if not a_element:
                continue
            detail_url = a_element["href"]
            detail_name = a_element.text

            process = multiprocessing.Process(target=worker, args=(detail_url, detail_name, cells[2].text, cells[3].text, cells[4].text))
            process.start()

        page += 1
    crawl = CrawlNhomDichVuCong()
    crawl.crawl()
    crawl.process_thutuchanhchinh()
    