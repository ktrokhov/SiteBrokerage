from app import db, Brocker
import re, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


Tinkoff = "https://otzovik.com/reviews/brokerskiy_schet_v_ao_tinkoff_bank/"
VTB = "https://otzovik.com/reviews/brokerskoe_obsluzhivanie_vtb_24/"
BKS = "https://otzovik.com/reviews/broker_bks_russia_moscow/"
FINAM = "https://otzovik.com/reviews/broker_finam/"
Otkritie = "https://otzovik.com/reviews/brokerskiy_dom_otkritie_russia_moscow/"
Alfa = "https://otzovik.com/reviews/brokerskoe_obsluzhivanie_alfa-direkt/"
Zerich = "https://otzovik.com/reviews/brokerskaya_kompaniya_cerih_kepital_menedzhment_russia_moscow/"
Sber ="https://otzovik.com/reviews/servis_sberbank_broker/"

allLinks = [Tinkoff, VTB, BKS, FINAM, Otkritie, Alfa, Zerich, Sber]
for i in allLinks:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(i)
    browser.maximize_window()
    soup0 = BeautifulSoup(browser.page_source)

    NameBroker = soup0.find("h1", {"class": "product-name"})
    print(NameBroker.text)
    Marks = soup0.findAll("div", {"class": "legend-item"})
    AllCount = 0
    SumAll = 0
    for someParse in Marks:

        title0 = someParse.find('a')
        if title0:
            title = title0.get('title')
        else:
            title = someParse.find('span').get('title')

        RateCategoryE = title.find('Ужасно')
        if RateCategoryE == 0:
            RateOtzivE = re.findall('(\d+)', title)
            AllCount = AllCount + int(RateOtzivE[0])
            print(AllCount)
            SumAll = SumAll + int(RateOtzivE[0])
            print(SumAll)

        RateCategoryD = title.find('Плохо')
        if RateCategoryD == 0:
            RateOtzivD = re.findall('(\d+)', title)
            AllCount = AllCount + int(RateOtzivD[0])
            SumAll += int(RateOtzivD[0]) * 2

        RateCategoryC = title.find('Средне')
        if RateCategoryC == 0:
            RateOtzivC = re.findall('(\d+)', title)
            AllCount = AllCount + int(RateOtzivC[0])
            SumAll += int(RateOtzivC[0]) * 3

        RateCategoryB = title.find('Хорошо')
        if RateCategoryB == 0:
            RateOtzivB = re.findall('(\d+)', title)
            AllCount = AllCount + int(RateOtzivB[0])
            SumAll += int(RateOtzivB[0]) * 4

        RateCategoryA = title.find('Отлично')
        if RateCategoryA == 0:
            RateOtzivA = re.findall('(\d+)', title)
            AllCount = AllCount + int(RateOtzivA[0])
            SumAll += int(RateOtzivA[0]) * 5


    print(SumAll)
    print(AllCount)

    print(SumAll/AllCount)
    browser.close()

