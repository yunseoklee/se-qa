from selenium import webdriver

#browser = webdriver.Firefox()
driver = webdriver.Chrome() # 경로를 넣어주면됨

url = 'https://www.samsung.com/sec'
driver.get(url)