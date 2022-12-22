from Scrapers import ItemScraper

if __name__ == "__main__":
    item = input("Prompt the item : ")

    scraper = ItemScraper()

    name = scraper.getItem(item)['Name']
    pprice = scraper.getItem(item)['Perfect Price (Popular)']
    price = scraper.getItem(item)['Perfect Price']

    print(f"{name} | ↑ {pprice} | - {price}")

