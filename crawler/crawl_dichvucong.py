from selenium import webdriver
import bs4
import json
from urllib.parse import urlparse, parse_qs
import multiprocessing
import os
class CrawlNhomDichVuCong:
    def __init__(self):
        pass
    
    def crawl(self):
        url = "https://dichvucong.cantho.gov.vn/dich-vu-cong-truc-tuyen?p_p_id=thutuchanhchinh_WAR_uniportalportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_thutuchanhchinh_WAR_uniportalportlet_javax.portlet.action=searchThuTuc"
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")
        box_coquans = soup.find_all("div", {"class": "box-coquan"})
        tieudes = []
        dichvucongs = []
        for box_coquan in box_coquans:
            ul = box_coquan.find("ul")
            h2_tieude = box_coquan.find("div", {"class": "h2-tieude"})
            tieudes.append({"ten": h2_tieude.text.strip(), "id": len(tieudes) + 1})

            nhomdichvucongs = ul.findChildren("li", recursive=False)
            print(tieudes[-1])
            for nhomdichvucong in nhomdichvucongs:
                id = nhomdichvucong.get("id").replace("nhomDVC", "")
                a_element = nhomdichvucong.find("a")
                ten = a_element.text.strip()
                dichvucongs.append({
                    "id": id,
                    "ten": ten,
                })
                modal = nhomdichvucong.find_next_sibling("div", {"class": "remodal"})
                list_tx = modal.find("ul", {"class": "danhsach-tx"})
                current_dichvucongs = list_tx.findChildren("li", recursive=False)
                for current_dichvucong in current_dichvucongs:
                    id = current_dichvucong.get("id").replace("nhomDVC", "")
                    a_element = current_dichvucong.find("a")
                    ten = a_element.text.strip()
                    dichvucongs.append({
                        "id": id,
                        "ten": ten,
                        "parent_id": nhomdichvucong.get("id").replace("nhomDVC", "")
                    })
        with open("./data/tieude.json", "w", encoding="utf-8") as tieude_file:
            json.dump(tieudes, tieude_file, ensure_ascii=False)
            tieude_file.close()
        
        with open("./data/nhomdichvucong.json", "w", encoding="utf-8") as dichvucong_file:
            json.dump(dichvucongs, dichvucong_file, ensure_ascii=False)
            dichvucong_file.close()
        
        self.process_thutuchanhchinh()

    def process_thutuchanhchinh(self):

            with open ("./data/nhomdichvucong.json", "r", encoding="utf-8") as dichvucong_file:
                nhomdichvucongs = json.load(dichvucong_file)
                dichvucong_file.close()
            i = 0
            for nhomdichvucong in nhomdichvucongs:
                if "parent_id" not in nhomdichvucong.keys():
                    continue
                id = nhomdichvucong["id"]
                process = multiprocessing.Process(target=self.worker_process_thutuchanhchinh, args=(id, nhomdichvucong))
                process.start()
                i += 1
                if i % 4 == 0:
                    process.join()


    
    def worker_process_thutuchanhchinh(self, id, nhomdichvucong):
        url = f"https://dichvucong.cantho.gov.vn/dich-vu-cong-truc-tuyen?p_p_id=thutuchanhchinh_WAR_uniportalportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=2&_thutuchanhchinh_WAR_uniportalportlet_nhomId={id}&_thutuchanhchinh_WAR_uniportalportlet_javax.portlet.action=searchThuTuc"
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")
        table_body = soup.find("tbody", {"class": "table-data"})
        table_rows = table_body.find_all("tr")
        ids_thutuchanhchinh = []
        for row in table_rows:
            cells = row.find_all("td")
            if len(cells) == 1:
                continue
            a_element = cells[1].find("a")
            if not a_element:
                continue
            detail_url = a_element["href"]
            parsed = urlparse(detail_url)
            thutuc_id = parse_qs(parsed.query)['_thutuchanhchinh_WAR_uniportalportlet_maThuTuc'][0]
            thutuc_id = thutuc_id.strip()
            print(thutuc_id)
            ids_thutuchanhchinh.append(thutuc_id)
        for thutuchanhchinh_id in ids_thutuchanhchinh:
            try: 
                with open(f"./data/thutuchanhchinh/{thutuchanhchinh_id}.json", "r") as thutuchanhchinh_file:
                    data = json.load(thutuchanhchinh_file)
                    data["nhomdichvucong"] = {
                        "id": nhomdichvucong["id"],
                        "ten": nhomdichvucong["ten"]
                    }
                    thutuchanhchinh_file.close()
                with open(f"./data/thutuchanhchinh/{thutuchanhchinh_id}.json", "w", encoding="utf-8") as thutuchanhchinh_file:
                    json.dump(data, thutuchanhchinh_file, ensure_ascii=False)
                    thutuchanhchinh_file.close()

            except Exception as e:
                print(e)
                continue
                            
