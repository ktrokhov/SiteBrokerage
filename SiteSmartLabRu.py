from app import db, Brocker
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

VTB = "https://smart-lab.ru/brokers-rating/vtb"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(VTB)
browser.maximize_window()
soup0 = BeautifulSoup(browser.page_source)
name = soup0.find('h2')
print(name.text)
parseIt = soup0.findAll("table")
for i in parseIt:
    print("here")
    tmpForTd = i.findAll("td")
    for j in tmpForTd:
        print("LOLOLOL")
        test = j.find('td')
        if test == None:
            continue

        text = test.renderContents()
        ans = text.strip()
        print(ans)
        # if ans == 'Клиентов на смартлабе':
        #     i.findAll('td')
        #     print(i[1].text)
        #
        # if ans == 'Смартлаб рейтинг ()':
        #     i.findAll('td')
        #     print(i[1].text)

browser.close()
# page1 = "https://smart-lab.ru/brokers-rating/russia/page1/"
# page2 = "https://smart-lab.ru/brokers-rating/russia/page2/"
# page3 = "https://smart-lab.ru/brokers-rating/russia/page3/"
# page4 = "https://smart-lab.ru/brokers-rating/russia/page4/"
# AllPages = [page1, page2, page3, page4]
# for i in AllPages:
#     browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser.get(i)
#     browser.maximize_window()
#     soup0 = BeautifulSoup(browser.page_source)
#     parse = soup0.findAll("div", {"class": "my_table_tr my_box my_box-center my_box--between"})
#     for j in parse:
#         tmpForName = j.find("div", {"class": "tr_item tr_item_name"})
#         Name = tmpForName.find('img').get('alt')
#         print(Name)
#         test = tmpForName.find('span')
#         print(test.text)
#         tmpForActiveClient = j.find("div", {"class": "tr_item tr_item_client_count"})
#         ActiveClient = tmpForActiveClient.find('span', {"class": "td_value"})
#         print(ActiveClient.text)
#         tmpForRate = j.find("div", {"class": "tr_item tr_item_raiting"})
#         Rate = tmpForRate.find('a')
#         print(Rate.text)
#
#
