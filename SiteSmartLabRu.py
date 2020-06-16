from app import db, Brocker
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

VTB = "https://smart-lab.ru/brokers-rating/vtb"
Tinkoff = "https://smart-lab.ru/brokers-rating/tinkoff-broker"
Sber = "https://smart-lab.ru/brokers-rating/sberbank-broker"
Finam = "https://smart-lab.ru/brokers-rating/finam"
Aton = "https://smart-lab.ru/brokers-rating/aton"
BCS = "https://smart-lab.ru/brokers-rating/bcs"
Otrkitie = "https://smart-lab.ru/brokers-rating/otkritie-broker"
Alfa = "https://smart-lab.ru/brokers-rating/alfa-direct"
FFin = "https://smart-lab.ru/brokers-rating/freedom-finance"
GazProm = "https://smart-lab.ru/brokers-rating/gazprombank"
Alor = "https://smart-lab.ru/brokers-rating/alor-broker"
Region = "https://smart-lab.ru/brokers-rating/region-broker"
# Raiff = "https://smart-lab.ru/brokers-rating/raiffeisen-broker"
PSB = "https://smart-lab.ru/brokers-rating/promsvyzbank-broker"
KitFin = "https://smart-lab.ru/brokers-rating/kit-finans"
InvestPal = "https://smart-lab.ru/brokers-rating/%D0%98%D0%BD%D0%B2%D0%B5%D1%81%D1%82%D0%B8%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%B0%D0%BB%D0%B0%D1%82%D0%B0"
Zerich = "https://smart-lab.ru/brokers-rating/zerich"
# RSHB = "https://smart-lab.ru/brokers-rating/rsgb-broker"
UralSib = "https://smart-lab.ru/brokers-rating/uralsib-capital"
Septem = "https://smart-lab.ru/brokers-rating/septem-capital"
Solid = "https://smart-lab.ru/brokers-rating/ifk-solid"
# AKBars = "https://smart-lab.ru/brokers-rating/AK-BARS-broker"
Rikom = "https://smart-lab.ru/brokers-rating/rikom-trust"
QBF = "https://smart-lab.ru/brokers-rating/QBF"
Veles = "https://smart-lab.ru/brokers-rating/%D0%92%D0%B5%D0%BB%D0%B5%D1%81%20%D0%9A%D0%B0%D0%BF%D0%B8%D1%82%D0%B0%D0%BB"
Univer = "https://smart-lab.ru/brokers-rating/univer-capital"
Reness = "https://smart-lab.ru/brokers-rating/%D0%A0%D0%B5%D0%BD%D0%B5%D1%81%D1%81%D0%B0%D0%BD%D1%81%20%D0%9A%D0%B0%D0%BF%D0%B8%D1%82%D0%B0%D0%BB"
ItCap = "https://smart-lab.ru/brokers-rating/ITI-Capital"

AllLinks = [VTB, Tinkoff, Sber, Finam, Aton, BCS, Otrkitie,
            Alfa, FFin, GazProm, Alor, Region, PSB, KitFin,
            InvestPal, Zerich, UralSib, Septem, Solid,
            Rikom, QBF, Veles, Univer, Reness, ItCap]
allBrkNames = ['ВТБ Капитал Брокер', 'Тинькофф Банк', 'ПАО Сбербанк', 'Инвестиционный Банк "ФИНАМ"',
               'ООО "АТОН"', 'Компания "Брокеркредитсервис"', 'Банк "Финансовая Корпорация Открытие"',
               'АО "АЛЬФА-БАНК"',
               'ООО Инвестиционная компания "Фридом Финанс"', 'АО "Газпромбанк"', 'ООО "АЛОР +"',
               'ООО "Брокерская компания "РЕГИОН"', 'ПАО "Промсвязьбанк"', 'АО "КИТ Финанс"',
               'ООО "Инвестиционная палата"',
               'АО Инвестиционная Компания "ЦЕРИХ Кэпитал Менеджмент"',
               'ООО "УРАЛСИБ Брокер"',
               'ООО Инвестиционная компания "Септем Капитал"' 'АО Инвестиционно - финансовая компания "Солид"',
               'АО Инвестиционная компания "РИКОМ-ТРАСТ"',
               'ООО Инвестиционная Компания «КьюБиЭф»',
               'ООО "ИК ВЕЛЕС Капитал"', 'ООО "УНИВЕР Капитал"', 'ООО "Ренессанс Брокер"', 'ООО "УНИВЕР Капитал"']

allRateBroker = []

for links in AllLinks:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(links)
    browser.maximize_window()
    soup0 = BeautifulSoup(browser.page_source)
    # Название Брокера
    name = soup0.find('h2')
    print(name.text)
    parseIt = soup0.findAll("div", {"class": "broker-info"})
    Rate = ''
    CountCilent = ''
    flagForRate = 0
    flagForClient = 0
    for i in parseIt:
        tmpForTd = i.findAll("td")
        for j in tmpForTd:

            if flagForClient == 1:
                flagForClient = -1
                for tmp in j.text:
                    if tmp != ' ':
                        CountCilent += tmp
                    else:
                        break
                print(int(CountCilent))
                break

            if flagForRate == 2:
                flagForRate = -1
                for tmp in j.text:
                    if tmp != ' ':
                        Rate += tmp
                    else:
                        break
                print(Rate)

            if j.text == 'Клиентов на смартлабе':
                flagForClient = 1

            if j.text == 'Смартлаб рейтинг (?)':
                flagForRate = 2

    # Формула
    intCountClient = int(CountCilent)
    intNewRate = 0
    flag = 0
    if Rate[0] == '+':
        flag = 1
        newRate = Rate.replace("+", "")
    else:
        flag = -1
        newRate = Rate.replace("-", "")

    intNewRate = int(newRate)

    if flag == 1:
        badRate = (intCountClient - intNewRate) / 2
        goodRate = badRate + intNewRate
    else:
        goodRate = (intCountClient - intNewRate) / 2
        badRate = goodRate + intNewRate

    ans = (goodRate * 5 + badRate) / intCountClient
    tmpDecimal = float('{:.2f}'.format(ans))
    print(tmpDecimal)
    allRateBroker.append(tmpDecimal)
    # time.sleep(15)
    browser.close()

for i, j in zip(allBrkNames, allRateBroker):
    UpdTable = Brocker.query.filter_by(name=i).update({'SiteSmartLabRU': j})
    db.session.commit()
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
