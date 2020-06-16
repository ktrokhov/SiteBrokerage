import re

# Links = ['Тинькофф Банк', 'ВТБ Капитал Брокер', 'Компания "Брокеркредитсервис"', 'Инвестиционный Банк "ФИНАМ"', 'Банк "Финансовая Корпорация Открытие"', 'АО "АЛЬФА-БАНК"', 'АО Инвестиционная Компания "ЦЕРИХ Кэпитал Менеджмент"', 'ПАО Сбербанк']
# Rate = [2.9565217391304346, 2.3, 1.4285714285714286, 2.5238095238095237, 2.225, 3.0, 3.3333333333333335, 2.0]
#
#
# for i, j in zip(Links, Rate):
#     test = float('{:.2f}'.format(j))
#     print(i, test)

# Rate = '-32 '
# CountCilent = 932
# intNewRate = 0
# flag = 0
# if Rate[0] == '+':
#     flag = 1
#     newRate = Rate.replace("+", "")
# else:
#     flag = -1
#     newRate = Rate.replace("-", "")
#
#
# intNewRate = int(newRate)
#
# if flag == 1:
#     badRate = (CountCilent - intNewRate)/2
#     goodRate = badRate + intNewRate
# else:
#     goodRate = (CountCilent - intNewRate) / 2
#     badRate = goodRate + intNewRate
#
#
# ans = (goodRate * 5 + badRate)/CountCilent
# tmpDecimal = float('{:.2f}'.format(ans))
# print(tmpDecimal)