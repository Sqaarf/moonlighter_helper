import requests
from bs4 import BeautifulSoup as bs

class ItemScraper:
    def __init__(self) -> None:
        self.page = requests.get("https://steamcommunity.com/sharedfiles/filedetails/?id=1757126124")
        self.soup = bs(self.page.text, "html.parser")
        self.item_list = self.initItemList()
        
    
    def initItemList(self) -> list:
        tr_tags = self.soup.find_all("div", attrs={"class": "bb_table_tr"})[:242]
        td_tags = []

        for tr_tag in tr_tags:
            td_tags.append(tr_tag.find_all("div", attrs={"class": "bb_table_td"}))

        keys_list = [key.text for key in td_tags[0]]

        ret = []
        index = 0

        for entry in td_tags:
            if entry[0].text == "Name":
                    continue
            else:
                ret.append({})
                for i in range(len(entry)):
                        ret[index][keys_list[i]] = entry[i].text
                index += 1
        
        return ret

    def getItem(self, item) -> dict:
        for entry in self.item_list:
            if entry["Name"] == item:
                return entry
                
