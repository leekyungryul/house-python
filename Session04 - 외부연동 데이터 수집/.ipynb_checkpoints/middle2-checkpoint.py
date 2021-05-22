#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
from selenium import webdriver
import bs4
import requests
import pandas as pd 


### 2. 웹브라우저 설정 및 브라우저 팝업

options = webdriver.ChromeOptions()
# 헤드리스 옵션 / 일반옵션
# 헤드리스 = 브라우저를 띄우지 않고 작업
options.add_argument("window-size=1920x1080") 
# pypi.org

driverLoc = "../addon/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(executable_path=driverLoc, options = options)

driver.implicitly_wait(5)

### 3. 브라우저 열기

targeturl = "http://www.ssg.com/"

driver.get(targeturl)

##### '#'은 ID '.'은 클래스를 의미한다.

### 4. 브라우저 내 액션(클릭)

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

Keywords = "아이맥"
keywordPath = '//*[@id="ssg-query"]'
# 쌍따움표를 사용중이므로 홑따움표로 감싼다.
keywordElement = driver.find_element_by_xpath(keywordPath)
action = ActionChains(driver)
action.move_to_element(keywordElement)

action.click()

# Keywords를 입력한다.
action.send_keys(Keywords)

action.send_keys(Keys.ENTER)

action.perform()

import time
html = driver.page_source
driver.current_url
driver.page_source
bs = bs4.BeautifulSoup(html, 'html.parser')
productList = bs.findAll(name="li", attrs={"class":"cunit_t232"})

# productName2 = litags.find(name="em", attrs={"class":"tx_en"})

# productprice = productList[0].find(name="em", attrs={"class":"ssg_price"})

# productprice.text

# len(productList)

# NameList = []
# PriceList = []
# for i in range(0,len(productList)):
#     Nametags = productList[i].find(name="div", attrs={"class":"title"})
#     productprice = productList[i].find(name="em", attrs={"class":"ssg_price"})
#     productName = Nametags.find(name="em", attrs={"class":"tx_en"})
    
#     NameList.append(productName.text)
#     PriceList.append(productprice.text)
# pd.DataFrame(zip(NameList,PriceList),columns = ["제품명","제품가격"])

columns = []
rows = []
for i in range(0,len(productList)):
    Nametags = productList[i].find(name="div", attrs={"class":"title"})
    productprice = productList[i].find(name="em", attrs={"class":"ssg_price"})
    productName = Nametags.find(name="em", attrs={"class":"tx_en"})
    
    columns.append(productName.text)
    columns.append(productprice.text)
    rows.append(columns)
    columns = []
# print(columns)   
# print(rows)
result = pd.DataFrame(rows)
result.to_csv("./imac_result.csv", index=False, encoding="ms949")
result.columns = ["제품명","가격"]
result
# result.columns["목록"]
# result.columns["제품명","가격"]


# SMTP 프로토콜 로드
import smtplib

# 이메일을 간단하게 보낼수 있는 라이브러리 로드
from email.message import EmailMessage

# import pickle
# pw = "password"    
# pickle.dump(pw, open("pw.pickle", 'wb'))
# pw = pickle.load(open('pw.pickle', 'rb'))

# GMAIL 메일 설정
smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)

# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()
 
# 연결을 암호화
smtp_gmail.starttls()

# userid = "haiteamm@gmail.com"
# import getpass
# mypass = getpass.getpass()
# userpw = mypass

#로그인 아이디 / 앱 비밀번호

# import getpass
# userpw = getpass.getpass()
# # 테스트용이지 실제론 쓸일없다

userid = "leekyung1111"
userpw = "gyqreowyutvvlbbk"
smtp_gmail.login(userid, userpw)

msg=EmailMessage()

# 제목 입력
msg['Subject']="아이맥 가격정보"
 
# 내용 입력
msg.set_content("아이맥최신상품")
 
# 보내는 사람
msg['From']='leekyung1111@gmail.com'
 
# 받는 사람
msg['To'] = 'leekyung1111@gmail.com'

# 첨부파일 추가
file='imac_result.csv'
fp = open(file,'rb')
file_data=fp.read()
msg.add_attachment(file_data,
                   maintype='text',
                   subtype='plain',
                   filename=file)
# 메일 전송
smtp_gmail.send_message(msg)
smtp_gmail.close()


# In[ ]:




