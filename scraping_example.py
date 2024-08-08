# scraping example for watch postings: 시계 판매글 수집하기

"""
props to
https://velog.io/@mino0121/Python-Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-Naver-cafe-%EA%B2%8C%EC%8B%9C%EB%AC%BC-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91

for an excellent guide
"""
# imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from collections import deque
import pyperclip
import json
import pickle



op = webdriver.ChromeOptions()
chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=op)

# logging in to the account: note that separate account without 2FA may be needed
keydir = "C:\\Projects\\Github\\key.txt"
with open(keydir, 'r') as file:
    data = file.read()

keyfob = json.loads(data)
nav_id, nav_pass = keyfob['id'], keyfob['pass']

driver.get("https://nid.naver.com/nidlogin.login")
time.sleep(3)
# Locate the ID input field and enter the ID
id_input = driver.find_element(By.CSS_SELECTOR, '#id')

# core logic for login: somehow the normal send_keys lead to incorrect login
# so pyperclip must be used
try:
    driver.find_element(By.CSS_SELECTOR,'#id')
    time.sleep(2)

    pyperclip.copy(nav_id)
    driver.find_element(By.CSS_SELECTOR,'#id').send_keys(Keys.CONTROL+'v')
    time.sleep(3)

    pyperclip.copy(nav_pass)
    secure = 'blank'
    driver.find_element(By.CSS_SELECTOR,'#pw').send_keys(Keys.CONTROL + 'v')
    pyperclip.copy(secure)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
    time.sleep(5)
    print("login successful")
except:
    print("App was unable to login correctly")


# 시계거래소 롤렉스 안전거래:  //*[@id="menuLink33"]
# 시계거래소 롤렉스 거래:  //*[@id="menuLink832"]

# 시계거래소 크롤링


driver.get('https://cafe.naver.com/sweetdressroom')
time.sleep(5)
board_paths = ['//*[@id="menuLink33"]', '//*[@id="menuLink832"]']


# Function to extract listings from a board
def extract_listings_from_board(board_link):
    driver.get(board_link)
    time.sleep(5)

    listings = driver.find_elements(By.CSS_SELECTOR, 'css_selector_for_listing_links')  # Adjust selector
    listing_links = [listing.get_attribute('href') for listing in listings]

    return listing_links


all_listings = []

for board in board_paths:
    tgt = driver.find_element(By.XPATH, board)
    driver.implicitly_wait(2)
    tgt.click()

    driver.switch_to.frame('cafe_main')

    driver.find_element(By.XPATH, '//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a[1]').click()
    time.sleep(1000)


# works up to this point

brand_list = ['오메가', '태그호이어', '롤렉스', '브레게', '바쉐론', '랑에', '파텍필립', '오데마피게']

# 브랜드를 순회하면서 https://cafe.naver.com/ca-fe/home/search/c-articles?q={검색어} 로 검색 후 크롤링
# > 로그인 불필요



# rolex listing search https://cafe.naver.com/ca-fe/home/search/c-articles?q=%EB%A1%A4%EB%A0%89%EC%8A%A4
# > need to rotate keywords to find each of the listing and append them as needed
# > select priority based on time; remove duplicate listings at processing time


