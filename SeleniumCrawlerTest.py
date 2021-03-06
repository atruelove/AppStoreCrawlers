import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 8)
    return driver
 
 
def lookup(driver, query, url, file):
    driver.get(url)
    time.sleep(5)
    try:
        app = driver.find_element_by_class_name("id-app-title")
        json.dump(app.text, file)
        file.write('\n')
        details = driver.find_element_by_css_selector('.details-section.reviews')
        expand = details.find_element_by_css_selector('.expand-button.expand-next')
        expand.click()
        i=0
        counter = 0
        while i<100:
            reviews = driver.find_elements_by_css_selector('.single-review')
            for review in reviews:
                author  = review.find_element_by_css_selector('.author-name')
                date = review.find_element_by_css_selector('.review-date')
                stars = review.find_element_by_css_selector('.star-rating-non-editable-container')
                rtext = review.find_element_by_css_selector('.review-body.with-review-wrapper')
                if date.text:
                    ptext = rtext.get_attribute('innerHTML')
                    out = {'Author' : author.text, 'Date' : date.text, 'Stars' : stars.get_attribute('aria-label'), 'Text' : ptext[36:-136]}
                    json.dump(out, file)
                    file.write('\n')
                    counter = counter + 1
            time.sleep(2)
            i = i + 1 
            expand.click()
        finalCount = app.text+': Number of reviews: '+str(counter)+'\n'
        file.write(finalCount)
        
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    file = open('GPReviewsTest.json', 'w')
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.amazon.dee.app', file)
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.insteon.insteon3', file)
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.nest.android', file)
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.philips.lighting.hue2', file)
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.belkin.wemoandroid', file)
    lookup(driver, "Selenium", 'https://play.google.com/store/apps/details?id=com.unikey.kevo', file) 
    time.sleep(5)
    driver.quit()
    file.close()
