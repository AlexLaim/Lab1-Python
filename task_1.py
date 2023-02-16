sum = float(input('Введите сумму\n'))
if sum < 0:
    print("Некорректный формат!"),
else:
    def dur(rub): return '{} руб. {:02d} коп.'.format(
        int(rub // 1), int(rub % 1 * 100))
    print(dur(sum))
