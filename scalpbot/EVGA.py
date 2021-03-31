import time
from selenium import webdriver
import classvariables

#for using Chrome
browser = webdriver.Chrome('C:\\Scalpbot\\chromedriver')

classwhendisabled = classvariables.classwhendisabled
classwhenactive = classvariables.classwhenactive

#bestbuy 3060 page

#NVIDIA GeForce RTX 3060 Ti 8GB GDDR6 Video Card (Founders)
#browser.get("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285")

#ZOTAC GeForce RTX 3060 Ti Twin Edge 8GB GDDR6 Video Card
#browser.get("https://www.bestbuy.ca/en-ca/product/zotac-geforce-rtx-3060-ti-twin-edge-8gb-gddr6-video-card/15178583")

#ZOTAC GeForce RTX 3060 Ti Twin Edge OC 8GB GDDR6 Video Card
#browser.get("https://www.bestbuy.ca/en-ca/product/zotac-geforce-rtx-3060-ti-twin-edge-oc-8gb-gddr6-video-card/15178452")

#MSI NVIDIA GeForce RTX 3060 Ti VENTUS 2X OC 8GB GDDR6 Video Card
#browser.get("https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3060-ti-ventus-2x-oc-8gb-gddr6-video-card/15178453")

#https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3060-ti-ftw3-ultra-8gb-gddr6-video-card/15200164
browser.get("https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3060-ti-ftw3-ultra-8gb-gddr6-video-card/15200164")



#bestbuy generic working page- test this code on some product page that has a working add to cart button
#browser.get("https://www.bestbuy.ca/en-ca/product/asus-28-4k-ultra-hd-60hz-1ms-gtg-tn-led-freesync-gaming-monitor-vp28uqgr-black/14539789")

buyButton = False

while not buyButton:
    
    try:
        #checks to see if button is disabled
        #IMPORTANT: rename this class by checking what the active class name is before running. Inspect element on a product that is not available, inspect element on the button> one of the classes that is very unique to the DISABLED button
        addToCartBtn = addButton = browser.find_element_by_class_name(classwhendisabled)
        
        #print console log if button not active
        print("Button is not ready yet")

        #refresh if button not active
        time.sleep(1)
        browser.refresh()

    except:
        #checks to see if button is enabled
        #IMPORTANT: rename this class by checking what the active class name is before running. Inspect element on a product that is not available, inspect element on the button> one of the classes that is very unique to the WORKING button
        addToCartBtn = addButton = browser.find_element_by_class_name(classwhenactive)

        #if button is active, clicks on it
        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True

