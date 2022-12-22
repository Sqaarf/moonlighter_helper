from Scrapers import ItemScraper

if __name__ == "__main__":
    scraper = ItemScraper()

    while True:
        item = input("Prompt the item : ")

        if item == "exit" or item == "":
            break

        if scraper.getItem(item) == None:
            print("Error : No item existing in this name")
            continue

        name = scraper.getItem(item)['Name']
        pprice = scraper.getItem(item)['Perfect Price (Popular)']
        price = scraper.getItem(item)['Perfect Price']

        print(f"{name} | ↑ {pprice} | - {price}")

