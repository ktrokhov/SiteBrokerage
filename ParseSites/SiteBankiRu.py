from app import db, Brocker
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from decimal import Decimal

allBrokerNames = ['Тинькофф Банк', 'ПАО Сбербанк', 'ВТБ Капитал Брокер', 'Компания "Брокеркредитсервис"',
             'Инвестиционный Банк "ФИНАМ"', 'Банк "Финансовая Корпорация Открытие"', 'АО "АЛЬФА-БАНК"', 'ООО "АТОН"',
             'ООО Инвестиционная компания "Фридом Финанс"', 'АО "Газпромбанк"', 'УК Альфа-Капитал', 'ООО "АЛОР +"',
             'ООО "Брокерская компания "РЕГИОН"', 'ПАО "Промсвязьбанк"', 'АО Инвестиционная компания "АЙ ТИ ИНВЕСТ"', 'АО "КИТ Финанс"',
             'ООО Инвестиционная компания "Септем Капитал"', 'ООО "Инвестиционная палата"',
             'АО Инвестиционная Компания "ЦЕРИХ Кэпитал Менеджмент"', 'АО "Российский Сельскохозяйственный банк"', 'АО "Сургутнефтегазбанк"',
             'ООО "УРАЛСИБ Брокер"', 'АО "Райффайзенбанк"', 'АО Инвестиционно - финансовая компания "Солид"', 'АО коммерческий банк "Ситибанк"',
             'ПАО Акционерный коммерческий банк "АК БАРС"', 'ООО Инвестиционная Компания «КьюБиЭф»', 'АО Инвестиционная компания "РИКОМ-ТРАСТ"',
             'ООО "ИК ВЕЛЕС Капитал"', 'ООО "Ренессанс Брокер"', 'ООО "УНИВЕР Капитал"', 'ПАО "Совкомбанк"', 'ПАО "Росбанк"']



link = "https://www.banki.ru/services/responses/championship/?date=2020&product=investments"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(link)
browser.maximize_window()
soup0 = BeautifulSoup(browser.page_source)
TmpParse = soup0.findAll("div", {"class": "hor-not-fit-element__content"})
test = soup0.find("td", {"ng-bind": "item.middleGrade|number:2"})
test2 = soup0.findAll("tbody", {"class": "first-half banks-list"})
test3 = soup0.findAll("tr", {"class": "item ng-scope"})
# print(test3)
for i in test3:
    StrName = ''
    Name = i.find("a", {"class": "ng-binding"})
    print(Name.text)
    StrName = Name.text
    Rate = i.find("td", {"ng-bind": "item.middleGrade|number:2"})
    # print(Rate.text)
    converToDecimal = Decimal(Rate.text.replace(',', '.'))
    print(converToDecimal)
    if re.search(r'\bБанк\b', StrName):
        StrName = re.sub('\Банк', '', StrName)
        print(StrName)
    for j in allBrokerNames:
        tmp = j.find(StrName)
        if tmp != -1:
            UpdTable = Brocker.query.filter_by(name=j).update({'SiteBankiRU': converToDecimal})
            db.session.commit()
            # print("Есть в списке")
            # print(StrName)
            break

    print("---------------------------------------")


browser.close()
#
# Tinkoff = "https://www.banki.ru/services/responses/bank/tcs/"
# VTB = "https://www.banki.ru/services/responses/bank/vtb/"
# Sber = "https://www.banki.ru/services/responses/bank/sberbank/"
# BKS = "https://www.banki.ru/services/responses/bank/bcs-bank/"
# Otkitie = "https://www.banki.ru/services/responses/bank/bcs-bank/"
# Alfa = "https://www.banki.ru/services/responses/bank/alfabank/"
# Gazprom = "https://www.banki.ru/services/responses/bank/gazprombank/"
# PBS = "https://www.banki.ru/services/responses/bank/promsvyazbank/"
# RSHB = "https://www.banki.ru/services/responses/bank/rshb/"
# UralSib = "https://www.banki.ru/services/responses/bank/uralsib/"
# Siti = "https://www.banki.ru/services/responses/bank/citibank/"
# AKBars = "https://www.banki.ru/services/responses/bank/akbars/"
# Reness = "https://www.banki.ru/services/responses/bank/rencredit/"
# SovKom = "https://www.banki.ru/services/responses/bank/rencredit/"
# RosBank = "https://www.banki.ru/services/responses/bank/rosbank/"
#
# AllLinks = [Tinkoff, VTB, Sber, BKS,
#             Otkitie, Alfa, Gazprom, PBS,
#             RSHB, UralSib, Siti, AKBars,
#             Reness, SovKom, RosBank]
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get(Tinkoff)
# browser.maximize_window()
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# soup0 = BeautifulSoup(browser.page_source)
# # Название брокера
# NameBroker = soup0.findAll("div", {"class": "header-h2 display-inline margin-right-x-small"})
# print(NameBroker[0].text)
# TmpCLickOnBrokerInfo = soup0.findAll("div", {"ng-show": "selectedTab == 'service-type'"})
# FindClick = TmpCLickOnBrokerInfo[0].findAll("li", {"ng-repeat": "item in typeOfPersonList.items"})
# for i in FindClick:
#     test = i.find('span')
#     print(test.text)
#     if test.text == 'Инвестиционные продукты / брокерское обслуживание':
#         clickIt = i.find("span", {"class": "ng-binding"})
#         # print(clickIt)
#         # clickIt.click()
#         print("GoodChoice")
#         # time.sleep(3)
#         break
#
# # Теперь обрабатываем оцеки
# HowManyPage = soup0.findAll("li", {"class": "ui-pagination__item ui-pagination__item--number"})
# print(HowManyPage[-1].text)
# Pages = HowManyPage[-1].text
# print(Pages)
# PageInt = (int(Pages))
# print(PageInt)
# CountArticle = 0
# SumMarks = 0
# k = 1
# for k in PageInt:
#     NewLink = Tinkoff + "?page=" + k
#     browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser.get(NewLink)
#     browser.maximize_window()
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     soup1 = BeautifulSoup(browser.page_source)
#     AllArticlesOnList = soup1.findAll("article", {"class": "responses__item"})
#     for j in AllArticlesOnList:
#         Mark = j.find("span", {"class": "responses-rating-grade"})
#         print(Mark.text)
#         CountArticle += 1
#         if Mark.text == '1':
#             SumMarks = SumMarks + int(Mark.text)
#
#         if Mark.text == '2':
#             SumMarks = SumMarks + int(Mark.text) * 2
#
#         if Mark.text == '3':
#             SumMarks = SumMarks + int(Mark.text) * 3
#
#         if Mark.text == '4':
#             SumMarks = SumMarks + int(Mark.text) * 4
#
#         if Mark.text == '5':
#             SumMarks = SumMarks + int(Mark.text) * 5
#
# print(NameBroker[0].text)
# print(SumMarks/CountArticle)
#
#
# browser.close()
