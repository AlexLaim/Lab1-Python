words = (
        input("\nВведите текст, который будет разбит на слова:\n")
        .replace(".", " ")
        .replace(",", " ")
        .split()
    )
wordsSeven = []
wordsFourToSeven = []
wordsOther = []
for i in range(len(words)):
    if len(words[i]) > 7:
        wordsSeven.append(words[i])
    elif len(words[i]) > 3 and len(words[i]) <= 7:
        wordsFourToSeven.append(words[i])
    else:
        wordsOther.append(words[i])

print("Все слова длинной более 7 символов:\n", *wordsSeven)
print("Все слова длинной от 4 до 7 символов:\n", *wordsFourToSeven)
print("Все остальные слова:\n", *wordsOther)