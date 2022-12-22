from Scrapers import ItemScraper

if __name__ == "__main__":
    scraper = ItemScraper()
    
    while True:
        item = input("Prompt the item : ")

        if item == "exit" or item == "":
            break

        name = scraper.getItem(item)['Name']
        pprice = scraper.getItem(item)['Perfect Price (Popular)']
        price = scraper.getItem(item)['Perfect Price']

        print(f"{name} | ↑ {pprice} | - {price}")

