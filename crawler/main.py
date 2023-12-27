import selenium
import bs4

from selenium import webdriver

driver = webdriver.Chrome()
page = 1
url = f"https://dichvucong.cantho.gov.vn/dich-vu-cong-truc-tuyen?p_p_id=thutuchanhchinh_WAR_uniportalportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_thutuchanhchinh_WAR_uniportalportlet_loaiDichVuBuuDien=-1&_thutuchanhchinh_WAR_uniportalportlet_mucDo=0&_thutuchanhchinh_WAR_uniportalportlet_tenThuTuc=&_thutuchanhchinh_WAR_uniportalportlet_iddonvi=0&_thutuchanhchinh_WAR_uniportalportlet_idCoQuan=0&_thutuchanhchinh_WAR_uniportalportlet_maLinhVuc=&_thutuchanhchinh_WAR_uniportalportlet_capThucHien=-1&_thutuchanhchinh_WAR_uniportalportlet_nhomId=0&_thutuchanhchinh_WAR_uniportalportlet_delta=20&_thutuchanhchinh_WAR_uniportalportlet_keywords=&_thutuchanhchinh_WAR_uniportalportlet_advancedSearch=false&_thutuchanhchinh_WAR_uniportalportlet_andOperator=true&_thutuchanhchinh_WAR_uniportalportlet_resetCur=false&_thutuchanhchinh_WAR_uniportalportlet_cur={page}"
driver.get(url)

while True:
    print("Crawling page ", page)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    table_body = soup.find("tbody", {"class": "table-data"})
    if not table_body:
        print("Completed at page", page)
        break
    table_rows = table_body.find_all("tr")
    for row in table_rows:
        cells = row.find_all("td")
    break