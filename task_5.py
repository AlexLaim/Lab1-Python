words = (
    input("\nВведите предложение, в котором все слова, начинающиеся с большой буквы, будут приведены к верхнему регистру:\n")
    .replace(",", " ")
    .split()
)
for i in range(len(words)):
    if words[i].istitle():
        print(words[i].upper(), end=" ")
    else:
        print(words[i], end=" ")
