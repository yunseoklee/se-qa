from Screenshot import Screenshot_Clipping
from selenium import webdriver

ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome('C:/Users/User/Downloads/aa/chromedriver')
url = "http://www.samsung.com/uk/mobile"
driver.get(url)

Hide_elements=['class=cl-sticky-navigation-text__wrap']
img_url=ob.full_Screenshot(driver, save_path=r'.',elements=Hide_elements, image_name='uk.png')
print(img_url)
driver.close()

driver.quit()