from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("12")[1].click()
browser.find_elements_by_link_text("15")[1].click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]").click()
browser.find_element_by_link_text("제주").click()

browser.find_element_by_link_text("항공권 검색").click()

# 해당 값이 나올때까지 기다림
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)
finally:
    pass
    # browser.quit()

# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")