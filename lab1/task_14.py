def non_empty(func):
    def wrapper():
        index = 0
        mas = func()
        for i in mas:
            if i == '':
                mas.pop(index)
            index+=1
        return mas
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())