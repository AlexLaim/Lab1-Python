card = input("Введите номер дебетовой карты:\n")
if card.isdigit() and len(card) == 16:
    for i in range(len(card)):
        if i > 3 and i <= 11:
            if i % 4 != 0:
                print("*", end="")
            else:
                print(" *", end="")
        else:
            if i == 12:
                print(" " + card[i], end="")
            else:
                print(card[i], end="")
else:
    print("Некорректный формат!")
