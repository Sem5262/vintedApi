import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class Browser:
    def __init__(self, vpn_path=None):
        if vpn_path:
            self.options = Options()
            self.options.add_extension(vpn_path)
            self.browser = webdriver.Chrome(options=self.options)
            input("Set Up your VPN")
        
        self.browser.get('https://vinted.be/')
            

    def get(self, url):
       
        self.browser.get(url)
        return json.loads(self.browser.find_element(By.TAG_NAME, 'pre').text)
    
class VintedApi():
    def __init__(self):
        self.searchBrowsers = []
        self.itemBrowsers = []

        self.currentSearchBrowser = 0
        self.currentItemsearchBrowser = 0

        self.lastIds = []
        self.timeout = 0.3

        self.searchUrl = 'https://www.vinted.be/catalog?search_text=&brand_ids[]=362&price_to=30.0&currency=EUR&search_id=12460601314&order=newest_first'

    def addSearchBrowser(self, vpn_path=None):
        try:
            browser = Browser(vpn_path=vpn_path)
        except Exception as e:
            print(e)
        self.searchBrowsers.append(browser)
    def deleteSearchBrowser(self, index):
        del self.searchBrowsers[index]

    def addItemBrowser(self, vpn_path):
        try:
            browser = Browser(vpn_path)
        except Exception as e:
            print(e)
        self.itemBrowsers.append(browser)
        
    def deleteItemBrowser(self, index):
        del self.itemBrowsers[index]

    def search(self):
        newIds = self.searchForNewItems()
        result = []
        for id in newIds:
            result.append(self.itemSearch(id))

    def itemSearch(self, item_id):
        if self.currentItemsearchBrowser == len(self.itemBrowsers) - 1:
            self.currentItemsearchBrowser = 0
        else:
            self.currentItemsearchBrowser += 1

        data  = self.itemBrowsers[self.currentItemsearchBrowser].get('https://www.vinted.be/api/v2/items/' + item_id +'?localize=true')['item']

        shortdata = {
            "title": data['title'],
            "description": data['description'],
            "url": data['url'],
            "price_numeric": data['price_numeric'],
            "total_item_price": data['total_item_price'],
            "currency": data['currency'],
            "size": data['size'],
            "country_title": data['country_title'],
            "brand": data['brand'],
            "feedback_reputation": data['user']['feedback_reputation'],
            "feedback_count": data['user']['feedback_count'],
            "photos" : [photo['full_size_url'] for photo in data['photos']]
        }
        return shortdata
    
    def itemSearchRaw(self, item_id):
        if self.currentItemsearchBrowser == len(self.itemBrowsers) - 1:
            self.currentItemsearchBrowser = 0
        else:
            self.currentItemsearchBrowser += 1

        data  = self.itemBrowsers[self.currentItemsearchBrowser].get('https://www.vinted.be/api/v2/items/' + item_id +'?localize=true')['item']

        return data

    
    def searchForNewItems(self):
        if self.currentSearchBrowser == len(self.searchBrowsers) - 1:
            self.currentSearchBrowser = 0
        else:
            self.currentSearchBrowser += 1

        # if page isn't loaded yet
        if self.searchBrowsers[self.currentSearchBrowser].browser.current_url != self.searchUrl:
            self.searchBrowsers[self.currentSearchBrowser].browser.get(self.searchUrl)

            try:
                WebDriverWait(self.searchBrowsers[self.currentSearchBrowser].browser, 30).until(
                    self.is_page_loaded
                )
                print("Page has completed loading.")
            except TimeoutException:
                print("Timed out waiting for the page to complete loading.")

        #page has already been loaded    
        else:
            self.searchBrowsers[self.currentSearchBrowser].browser.find_element(By.XPATH, '//*[@data-testid="catalog--sort-filter--trigger"]').click()
            # wait for button
            try:
                WebDriverWait(self.searchBrowsers[self.currentSearchBrowser].browser, 10).until(EC.element_to_be_clickable((By.ID, "sort_by-list-item-newest_first")))
            except TimeoutException:
                pass

            self.searchBrowsers[self.currentSearchBrowser].browser.find_element(By.ID, "sort_by-list-item-newest_first").click()


        try:
            WebDriverWait(self.searchBrowsers[self.currentSearchBrowser].browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.new-item-box__overlay')))
            WebDriverWait(self.searchBrowsers[self.currentSearchBrowser].browser, 10).until(
                self.no_ajax_elements
            )
        except TimeoutException:
            pass


        overlay_elements = self.searchBrowsers[self.currentSearchBrowser].browser.find_elements(By.CSS_SELECTOR, '.new-item-box__overlay')

        if self.lastIds != []:
            newItemsIds = []
            newLastIds = [overlay_element.get_attribute('href').split('/')[-1].split('-')[0] for overlay_element in overlay_elements[:5]]

            for overlay_element in overlay_elements:
                item_url = overlay_element.get_attribute('href')
                item_id = item_url.split('/')[-1].split('-')[0]

                if item_id in self.lastIds:
                    self.lastIds = newLastIds
                    return newItemsIds
                else:
                    newItemsIds.append(item_id)

                  
        else:
            self.lastIds = [overlay_element.get_attribute('href').split('/')[-1].split('-')[0] for overlay_element in overlay_elements[:5]]
            return []
        
    def is_page_loaded(driver):
        return driver.execute_script("return document.readyState === 'complete'")

    def no_ajax_elements(driver):
        elements = driver.find_elements(By.CSS_SELECTOR, '.ajax')
        return len(elements) == 0