from selenium import webdriver
import pyautogui as pyautogui

driver = webdriver.Chrome()

url = "http://www.samsung.com/sec"
driver.get(url)

pyautogui.moveTo(320,180,3)
pyautogui.click()
pyautogui.dragTo(100,200,button='left')
pyautogui.click(button='right')
pyautogui.moveTo(130,365,1)
#driver.close()
#driver.quit()