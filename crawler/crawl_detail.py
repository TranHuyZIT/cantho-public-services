from selenium import webdriver
from urllib.parse import urlparse, parse_qs
import json
import bs4
class DetailCrawler:
    def __init__(self, url, name, mucdo, linhvuc, coquanthuchien):
        self.url = url
        self.name = name.strip()
        self.mucdo = mucdo.strip()
        self.linhvuc = linhvuc.strip()
        self.coquanthuchien = coquanthuchien.strip()
        self.driver = webdriver.Chrome()
        parsed_url = urlparse(url)
        self.id = parse_qs(parsed_url.query)["_thutuchanhchinh_WAR_uniportalportlet_maThuTuc"][0]
    
    def crawl(self):
        try:
            print("Crawling detail", self.name)
            self.driver.get(self.url)
            html = self.driver.page_source
            soup = bs4.BeautifulSoup(html, "html.parser")
            info_rows = soup.find_all("div", {"class": "row info-row"})
            detail_data = self.extract_infos(info_rows)
            self.persist(detail_data)
        except Exception as e:
            self.log_error(e)
            
    def log_error(self, e):
        print("Error when crawling detail", self.name, e)
        with open("./data/thutuchanhchinh/error.txt", "a", encoding="utf-8") as error_file:
            error_file.write(f"{self.id},{self.name},{self.url},{str(e)}\n")

    def extract_infos(self, info_rows):
        id = self.get_value_from_row(info_rows[0])
        soqd = self.get_value_from_row(info_rows[1])
        ten = self.get_value_from_row(info_rows[2])
        capthuchien = self.get_value_from_row(info_rows[3])
        loaithutuc = self.get_value_from_row(info_rows[4])
        linhvuc = self.linhvuc
        trinhtuthuchien = self.get_value_from_row(info_rows[6], cls_name="col-sm-9 col-xs-12 cls-impl-orders")
        cachthucthuchiens = self.extract_cachthucthuchiens(info_rows[7])
        thanhphanhosos = self.extract_thanhphanhosos(info_rows[8])
        doituongthuchien = self.get_value_from_row(info_rows[9])
        coquanthuchien = self.get_value_from_row(info_rows[10])
        coquanthamquyen = self.get_value_from_row(info_rows[11])
        diachitiepnhanhs = self.get_value_from_row(info_rows[12])
        coquanuyquyen = self.get_value_from_row(info_rows[13])
        coquanphoihop = self.get_value_from_row(info_rows[14])
        ketquathuchien = self.get_value_from_row(info_rows[15])
        cancuphaplys = self.extract_cancuphaplys(info_rows[16])
        yeucaudieukien = self.get_value_from_row(info_rows[17])

        return {
            "id": id,
            "soqd": soqd,
            "ten": ten,
            "capthuchien": capthuchien,
            "loaithutuc": loaithutuc,
            "linhvuc": linhvuc,
            "trinhtuthuchien": trinhtuthuchien,
            "cachthucthuchiens": cachthucthuchiens,
            "thanhphanhosos": thanhphanhosos,
            "doituongthuchien": doituongthuchien,
            "coquanthuchien": coquanthuchien,
            "coquanthamquyen": coquanthamquyen,
            "diachitiepnhanhs": diachitiepnhanhs,
            "coquanuyquyen": coquanuyquyen,
            "coquanphoihop": coquanphoihop,
            "ketquathuchien": ketquathuchien,
            "cancuphaplys": cancuphaplys,
            "yeucaudieukien": yeucaudieukien
        }
    
    def extract_cachthucthuchiens(self, row):
        cachthucthuchiens = row.find("div", {"class": "col-sm-9 col-xs-12"})
        table_body = cachthucthuchiens.find("tbody")
        if table_body is None:
            return []
        table_rows = table_body.find_all("tr")
        data = []
        for row in table_rows:
            cells = row.find_all("td")
            if len(cells) == 1:
                data.append({
                    "ghichu": cells[0].text.strip(),
                })
                continue
            
            data.append({
                "hinhthucnop": cells[0].text.strip(),
                "thoigiangiaiquyet": cells[1].text.strip(),
                "phi": ''.join([str(child) for child in cells[2].contents]),
                "mota": cells[3].text.strip()
            })
        return data

    def extract_thanhphanhosos(self, row):
        cachthucthuchiens = row.find("div", {"class": "col-sm-9 col-xs-12"})
        table_body = cachthucthuchiens.find("tbody")
        if  table_body is None:
            return []
        table_rows = table_body.find_all("tr")
        data = []
        for row in table_rows:
            cells = row.find_all("td")
            if len(cells) == 1:
                data.append({
                    "ghichu": cells[0].text.strip(),
                })
                continue
            data.append({
                "ten": cells[0].text.strip(),
                "banchinh": cells[1].text.strip(),
                "bansao": cells[2].text.strip(),
                "maudon": ''.join([str(child) for child in cells[3].contents]),
            })
        return data


    def extract_cancuphaplys(self, row):
        cancuphaplys = row.find("div", {"class": "col-sm-9 col-xs-12"})
        table_body = cancuphaplys.find("tbody")
        if table_body is None:
            return []
        table_rows = table_body.find_all("tr")
        data = []
        for row in table_rows:
            cells = row.find_all("td")
            if len(cells) == 1:
                data.append({
                    "ghichu": cells[0].text.strip(),
                })
                continue
            data.append({
                "sokyhieu": cells[0].text.strip(),
                "trichyeu": cells[1].text.strip(),
                "ngaybanhanh": cells[2].text.strip(),
                "coquanbanhanh": cells[3].text.strip(),
            })
        return data

    def get_value_from_row(self, row, cls_name="col-sm-9 col-xs-12"):
        return row.find("div", {"class": cls_name}).text.strip()
    
    def persist(self, detail_data):
        with open(f"./data/thutuchanhchinh/{self.id}.json", "w", encoding="utf-8") as detail_json:
                json.dump(detail_data, detail_json, ensure_ascii=False)
        