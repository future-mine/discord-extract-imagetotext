from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
import json
from requests import get
import time
import os
import ast
import urllib.request
import random
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime

from imagetotext import *
from env import *



##########################################################################
# binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

# caps = DesiredCapabilities.FIREFOX.copy()
# caps['marionette'] = True
# driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps, executable_path= os.getcwd()+"\geckodriver.exe")

############################################################################
driver = webdriver.Chrome(ChromeDriverManager().install())
############################################################################

email = EMAIL
password = PASSWORD
channel = CHANNEL
guild = GUILD

url = "https://discord.com/login"
driver.get(url) 
while True:
    try:
        email_el = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
        pass_el = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
        login_butt = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')

        email_el.send_keys(email)
        pass_el.send_keys(password)

        login_butt.click()
        break
    except:
        time.sleep(1)

time.sleep(15)

channel_url = 'https://discord.com/channels/707492893845225533/707492893845225536'
channel_url = 'https://discord.com/channels/' + channel + '/' + guild
driver.get(channel_url)

time.sleep(15)
soup = BeautifulSoup(driver.page_source, 'html.parser')
items = soup.find_all('a',{'class':'anchor-3Z-8Bb anchorUnderlineOnHover-2ESHQB imageWrapper-2p5ogY imageZoom-1n-ADA clickable-3Ya1ho embedWrapper-lXpS3L'})

image_urls = []

for it in items:
    url = it['href']
    ptrarr = url.split('/')
    daytimestr = ptrarr[len(ptrarr)-1].split('.')[0]
    daystr = daytimestr.split('_')[0]
    date_object = datetime.datetime.strptime(daystr, '%Y-%m-%d').date()
    image_urls.append([date_object, it['href']])


textarr = []
for it in image_urls:
    date = it[0]
    imgurl = it[1]
    print(it)
    img_data = get(imgurl).content
    with open('data/ptr.png', 'wb') as handler:
        handler.write(img_data)
    imgstr = get_string('data/ptr.png')
    print(imgstr)
    textarr.append([date, imgstr])
today_text = []
today = datetime.date.today()
for it in textarr:
    if today == it[0]:
        today_text.append(it[1])
print(today_text)
driver.close()
def check_json(json):
    return True

def write(nums_get):
    t = time.localtime()
    current_time = time.strftime("%H_%M_S", t)
    file_name = current_time + '.xlsx'
    numb = []
    boolean = []
    for row in nums_get:
        numb.append(row[0])
        boolean.append(row[1])

    df = pd.DataFrame({'number':numb, 'check':boolean})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:

    # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, sheet_name='Sheet')
    writer.close()





