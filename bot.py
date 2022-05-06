from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

from textAlert import sendMail

def main():
    load_dotenv()
    email = os.getenv('USER_EMAIL')
    pw = os.getenv('USER_PASS')
    sms_gate = os.getenv('SMS_GATEWAY').split()
    urltest = "https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-with-triple-fan/6505083.p?skuId=6505083"
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('headless')
    options.add_argument(f'user-agent={user_agent}')
    #options.add_argument('window-size=1,1')
    driver = webdriver.Chrome(executable_path= PATH, options = options)
    #driver.set_window_position(-5000, 0)
    driver.get(url)

    isComplete = False
    inStock = False
    msg = "\nRTX 3070 FE IN STOCK\n" + url

    while not isComplete:
        try:
            cartBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
            )
        except:
            driver.refresh()
            print("Add to cart button not found")
            inStock = False
            continue

        if(not inStock):
            sendMail(msg, email, pw, sms_gate)
            print("In stock update. Sending out alert")
            inStock = True

if __name__ == "__main__":
    main()
    