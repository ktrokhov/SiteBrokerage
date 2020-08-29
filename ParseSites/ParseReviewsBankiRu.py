import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from app import db, Brocker

tink = 'https://www.banki.ru/services/responses/bank/tcs/city/moskva/product/investments/'
sber = 'https://www.banki.ru/services/responses/bank/sberbank/city/moskva/product/investments/'
vtb = 'https://www.banki.ru/services/responses/bank/vtb/city/moskva/product/investments/'
otkritie = 'https://www.banki.ru/services/responses/bank/fk_otkritie/city/moskva/product/investments/'
gazprom = 'https://www.banki.ru/services/responses/bank/gazprombank/city/moskva/product/investments/'
alfa = 'https://www.banki.ru/services/responses/bank/alfabank/city/moskva/product/investments/'
psb = 'https://www.banki.ru/services/responses/bank/promsvyazbank/city/moskva/product/investments/'
rshb = 'https://www.banki.ru/services/responses/bank/rshb/city/moskva/product/investments/'
raif = 'https://www.banki.ru/services/responses/bank/raiffeisen/city/moskva/product/investments/'
citi = 'https://www.banki.ru/services/responses/bank/citibank/city/moskva/product/investments/'
reness = 'https://www.banki.ru/services/responses/bank/rencredit/city/moskva/product/investments/'
sovkom = 'https://www.banki.ru/services/responses/bank/sovcombank/city/moskva/product/investments/'
rosbank = 'https://www.banki.ru/services/responses/bank/rosbank/city/moskva/product/investments/'

allSite = [tink, sber, vtb, otkritie, gazprom, alfa, psb, rshb, raif, citi, reness, sovkom, rosbank]
allBanks = ['Тинькофф Банк', 'ПАО Сбербанк', 'ВТБ Капитал Брокер', 'Банк "Финансовая Корпорация Открытие"',
            'АО "Газпромбанк"', 'АО "АЛЬФА-БАНК"', 'ПАО "Промсвязьбанк"', 'АО "Российский Сельскохозяйственный банк"',
            'АО "Райффайзенбанк"', 'АО коммерческий банк "Ситибанк"', 'ООО "Ренессанс Брокер"', 'ПАО "Совкомбанк"', 'ПАО "Росбанк"']

# browser = webdriver.Chrome(ChromeDriverManager().install())
alljson = []
for site in allSite:
    print(site)
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(site)
    browser.maximize_window()
    soup0 = BeautifulSoup(browser.page_source)
    allreviews = soup0.findAll('div', {'class': 'responses-list mobile-full-width'})
    countRev = 0
    counrMarks = 0
    # print(allreviews)
    massRev = []
    massMarks = []
    for i in allreviews:
        textRev = i.findAll('div', {'class': 'responses__item__message markup-inside-small markup-inside-small--bullet'})
        for j in textRev:
            countRev += 1
            if countRev == 11:
                break
            massRev.append(j.text)

        markRev = i.findAll('span', {'data-test': 'responses-rating-grade'})
        for mark in markRev:
            counrMarks += 1
            if counrMarks == 11:
                break
            massMarks.append(int(mark.text))

    a = {}
    a['rewies'] = []
    for k, m in zip(massRev, massMarks):
        b = {}
        b['text'] = k.replace('\t', '').replace('\n', '')
        b['marks'] = m
        a['rewies'].append(b)
        # print('{ "text":', k, ',"mark":', m, '},')

    # print("kek")
    # print(json.dumps(a))
    alljson.append(json.dumps(a['rewies']))
    time.sleep(1)
    browser.close()


for i, j in zip(allBanks, alljson):
    UpdTable = Brocker.query.filter_by(name=i).update({'Reviews': j})
    db.session.commit()