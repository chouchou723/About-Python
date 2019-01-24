
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome("D:/chromeDriver/chromedriver.exe")
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)
# -*- coding:UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome("D:/chromeDriver/chromedriver.exe",chrome_options=options)
    driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

    html = driver.page_source
    bf1 = BeautifulSoup(html, 'lxml')
    result = bf1.find_all(class_='singlePage')
    # print('result：%s' % result)

    bf2 = BeautifulSoup(str(result[0]), 'lxml')
    titleS = bf1.find(class_='doc-title')
    title = BeautifulSoup(str(titleS), 'lxml').div.text
    # num =1;page <4

    # pagenum = bf2.find_all(class_='size')
    # pagenum = BeautifulSoup(str(pagenum), 'lxml').span.string
    # pagepattern = re.compile('页数：(\d+)页')
    # num = int(pagepattern.findall(pagenum)[0])
    print('文章标题：%s' % title)
    # print('文章页数：%d' % num)

    num = 3
    while True:
        html = driver.page_source
        bf1 = BeautifulSoup(html, 'lxml')
        result = bf1.find_all(class_='singlePage')
        flag = 0
        for each_result in result:
            bf2 = BeautifulSoup(str(each_result), 'lxml')
            texts = bf2.find_all('p')
            for each_text in texts:
                main_body = BeautifulSoup(str(each_text), 'lxml')
                for each in main_body.find_all(True):
                    if each.name == 'span':
                        print(each.string.replace('\xa0',''),end='')
                    elif each.name == 'br':
                        print('')
            print('\n')
        try:
            page = driver.find_elements_by_xpath("//div[@class='btns-warp']")
            driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
            nextpage = driver.find_element_by_xpath("//div[@class='foldpagewg-text-con']")
            nextpage.click()
            time.sleep(3)
        except:
            pagea = driver.find_elements_by_xpath("//div[@class='pagerwg-root']")
            driver.execute_script('arguments[0].scrollIntoView();', pagea[-1]) #拖动到可见的元素去
            nextpagea = driver.find_element_by_xpath("//div[@class='pagerwg-button']")
            print(nextpagea,num)
            nextpagea.click()
            time.sleep(3)
        else:
            print('error')
        # print(abc)
        # if abc:
        #     page = driver.find_elements_by_xpath("//div[@class='btns-warp']")
        #     driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
        #     nextpage = driver.find_element_by_xpath("//div[@class='foldpagewg-text-con']")
        #     if(nextpage):
        #         nextpage.click()
            
        #     num = num - 1
        #     time.sleep(3)
        # elif driver.find_element_by_xpath("//div[@class='pagerwg-button']"):
        #     pagea = driver.find_elements_by_xpath("//div[@class='pagerwg-root']")
        #     driver.execute_script('arguments[0].scrollIntoView();', pagea[-1]) #拖动到可见的元素去
        #     nextpagea = driver.find_element_by_xpath("//div[@class='pagerwg-button']")
        #     print(nextpagea,num)
        #     if(nextpagea):
        #         nextpagea.click()

        #     num = num - 1
        #     time.sleep(3)
        # else:
        #     break