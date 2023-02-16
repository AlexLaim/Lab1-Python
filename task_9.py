import random

allMoney = random.randrange(10, 10000, 10)
thousands = allMoney//1000
hundreds = (allMoney - thousands*1000) // 100
fifties = (allMoney - thousands*1000 - hundreds*100)//50
dozens = (allMoney - thousands*1000 - hundreds*100 - fifties*50)//10
cash = {"1000": thousands, "100": hundreds, "50": fifties, "10": dozens}
print('Банкомат выдает купюры 1000, 100, 50, 10')
money = int(input('Введите количество снимаемых денег (не более 10000 за раз):\n'))

result = ""
if allMoney > money and money % 10 == 0:
    for action in cash.items():
        if money >= int(action[0]) and action[1] > 0:
           count = money//int(action[0])
           result += str(count) + "*" + action[0] + " + "
           cash.update({action[0]: cash.get(action[0]) - count})
           money -= count * int(action[0])
        if money == 0:
            print(result[:-2])
            break
else:
    print('Операция не может быть выполнена!')