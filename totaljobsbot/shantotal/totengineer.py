from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
#Basic AI- utilise variable input. The script reloads when the input changes.



ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

# Initiate the browser
# create instance of webdriver
#replace your chromedriver path
path='/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path, options=chrome_options)
url='https://www.totaljobs.com/account/signin?ReturnUrl=/'
driver.get(url)

loginemail='shan.lingeswaran@hotmail.co.uk'
passw='minimumwaste1'
time.sleep(2)
try:
    driver.find_element_by_id('ccmgt_explicit_accept').click()
    driver.find_element_by_name('Form.Email').send_keys(loginemail)
    driver.find_element_by_id('Form_Password').send_keys(passw)
    driver.find_element_by_id('btnLogin').click()
except:
    pass
role = "Engineer"#input("Enter the role you'd like to search for?")
where = "WD5"#input("Enter postcode/location?")
#range = input("Range? Choose from:0,5,10,20 & 30?")
sal = "60000"
o =''
d = role.split()
for i in d:
    o+= i + '-'
print(o[0:-1])

driver.get("https://www.totaljobs.com/jobs/" + o + "/in-" + where + "?salary=" + sal + "&salarytypeid=1&radius=5")

href=[]
links=[]
uniq=[]

def collectLynx():
    for a in driver.find_elements_by_xpath('.//a'):
        try:
            links.append(a.get_attribute('href'))
        except NoSuchElementException or StaleElementReferenceException:
            print(a)
            pass
    for val in links:
        if val != None:
            href.append(val)
    for i in range(0,len(href)):
        uniq.append(re.findall("\d+", href[i]))
    id=[]
    for val in uniq:
        if val != []:
            id.append(val)
    id1=[]
    for i in range(0,len(id)):
        if len(id[i][0])==8:
            id1.append(id[i][0])
    lyn=[]
    print(len(lyn))
    for i in id1:
        lyn.append('https://www.totaljobs.com/job/' + i + '/apply/oneclick?TemplateType=Standard')
        lyn.append('https://www.totaljobs.com/job/' + i + '/apply/oneclick?TemplateType=ResponsiveFeatured')
        lyn.append('https://www.totaljobs.com/job/' + i + '/apply/oneclick?TemplateType=ResponsivePremium')
    lyn1=list(set(lyn))

    x=1
    for i in lyn1:
        #quite primitive but does the ones which one click apply\! (what i was after)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.get(i)
        time.sleep(5)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
        print('sent'+str(x))
        x+=1
    else:
        print('Fail')
def nxtPag():
    page_number = 1

    while True:
        try:
            for i in range(1,100):
                link = "https://www.totaljobs.com/jobs/" + o + "/in-" + where + "?salary=" + sal + "&salarytypeid=1&radius=5&page="+str(i)
                time.sleep(5)
                collectLynx()
                time.sleep(5)
        except NoSuchElementException or StaleElementReferenceException:
                print('check')
                pass
        print(driver.current_url)

nxtPag()
