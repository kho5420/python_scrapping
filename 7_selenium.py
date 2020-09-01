from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

# 사이트 이동
browser.get("http://naver.com")

# 로그인 버튼
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id / pw 입력
browser.find_element_by_id("id").send_keys("kho54230")
browser.find_element_by_id("pw").send_keys("q15396139?2")

browser.find_element_by_id("log.login").click()

