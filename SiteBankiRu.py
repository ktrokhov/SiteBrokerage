from app import db, Brocker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

Tinkoff = "https://www.banki.ru/services/responses/bank/tcs/"
VTB = "https://www.banki.ru/services/responses/bank/vtb/"
Sber = "https://www.banki.ru/services/responses/bank/sberbank/"
BKS = "https://www.banki.ru/services/responses/bank/bcs-bank/"
Otkitie = "https://www.banki.ru/services/responses/bank/bcs-bank/"
Alfa = "https://www.banki.ru/services/responses/bank/alfabank/"
Gazprom = "https://www.banki.ru/services/responses/bank/gazprombank/"
PBS = "https://www.banki.ru/services/responses/bank/promsvyazbank/"
RSHB = "https://www.banki.ru/services/responses/bank/rshb/"
UralSib = "https://www.banki.ru/services/responses/bank/uralsib/"
Siti = "https://www.banki.ru/services/responses/bank/citibank/"
AKBars = "https://www.banki.ru/services/responses/bank/akbars/"
Reness = "https://www.banki.ru/services/responses/bank/rencredit/"
SovKom = "https://www.banki.ru/services/responses/bank/rencredit/"
RosBank = "https://www.banki.ru/services/responses/bank/rosbank/"

AllLinks = [Tinkoff, VTB, Sber, BKS,
            Otkitie, Alfa, Gazprom, PBS,
            RSHB, UralSib, Siti, AKBars,
            Reness, SovKom, RosBank]
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(Tinkoff)
browser.maximize_window()
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
soup0 = BeautifulSoup(browser.page_source)
# Название брокера
NameBroker = soup0.findAll("div", {"class": "header-h2 display-inline margin-right-x-small"})
print(NameBroker[0].text)
TmpCLickOnBrokerInfo = soup0.findAll("div", {"ng-show": "selectedTab == 'service-type'"})
FindClick = TmpCLickOnBrokerInfo[0].findAll("li", {"ng-repeat": "item in typeOfPersonList.items"})
for i in FindClick:
    test = i.find('span')
    print(test.text)
    if test.text == 'Инвестиционные продукты / брокерское обслуживание':
        clickIt = i.find("span", {"class": "ng-binding"})
        # print(clickIt)
        # clickIt.click()
        print("GoodChoice")
        # time.sleep(3)
        break

# Теперь обрабатываем оцеки
HowManyPage = soup0.findAll("li", {"class": "ui-pagination__item ui-pagination__item--number"})
print(HowManyPage[-1].text)
Pages = HowManyPage[-1].text
print(Pages)
PageInt = (int(Pages))
print(PageInt)
CountArticle = 0
SumMarks = 0
k = 1
for k in PageInt:
    NewLink = Tinkoff + "?page=" + k
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(NewLink)
    browser.maximize_window()
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    soup1 = BeautifulSoup(browser.page_source)
    AllArticlesOnList = soup1.findAll("article", {"class": "responses__item"})
    for j in AllArticlesOnList:
        Mark = j.find("span", {"class": "responses-rating-grade"})
        print(Mark.text)
        CountArticle += 1
        if Mark.text == '1':
            SumMarks = SumMarks + int(Mark.text)

        if Mark.text == '2':
            SumMarks = SumMarks + int(Mark.text) * 2

        if Mark.text == '3':
            SumMarks = SumMarks + int(Mark.text) * 3

        if Mark.text == '4':
            SumMarks = SumMarks + int(Mark.text) * 4

        if Mark.text == '5':
            SumMarks = SumMarks + int(Mark.text) * 5

print(NameBroker[0].text)
print(SumMarks/CountArticle)


browser.close()
