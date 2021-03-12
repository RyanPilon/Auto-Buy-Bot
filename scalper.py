import time
from selenium import webdriver
#for using chrome
browser = webdriver.Chrome('/home/ryan/Documents/projects/independent_projects/Auto-Buy-Bot/chromedriver')

#enter path below to item you wish to scalp
#browser.get("")

#Best Buy out of stock item
#browser.get("https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400")

#Best buy instock Item
browser.get("https://www.bestbuy.com/site/hp-omen-15-6-gaming-laptop-intel-core-i7-16gb-memory-nvidia-geforce-rtx-3070-512gb-ssd-shadow-black/6448615.p?skuId=6448615")


buy_button = False

while not buy_button:

    try:
        #inspect element on webpage for unique class when "out of stock" insert in ("")
        add_to_cart_btn = add_button = browser.find_element_by_class_name("btn-disabled")

        #button still disabled
        print("Item is still out of stock.")

        #waits 'n' seconds and retries
        time.sleep(1)
        browser.refresh()

    except:
        #inspect element on webpage for unique class when "in stock" insert in ("")
        add_to_cart_btn = add_button = browser.find_element_by_class_name("btn-primary")

        #once button is clicked, script is ended
        print("Item is in stocked and button clicked!")
        add_to_cart_btn.click()
        buy_button = True
