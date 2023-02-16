words = (
    input("\nВведите предложение, из которого будут выведены все символы по 1 разу на консоль:\n")
    .replace(",", " ")
    .split()
)
print("Символы в вашем предложении:")
for i in range(len(words)):
    for j in range(len(words[i])):
        print(words[i][j])