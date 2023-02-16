import re

while(True):
    password = input('Введите пароль на проверку (минимальная длина 10 символов) или слово "end" для завершения программы:\n')
    pattern1 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$'
    pattern2 = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{10,}$'
    if password == 'end':
        break
    if re.match(pattern1, password):
        print('Очень надежный пароль')
    elif re.match(pattern1, password):
        print('Пароль средней сложности')
    else:
        print('Ненадежный пароль, лучше выбрать другой')