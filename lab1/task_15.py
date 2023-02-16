def pre_process(a=0.97):
    def decor(func):
        def wrapper(arg):
            for i in range(len(arg)):
                arg[i] =arg[i]- a * arg[i - 1]
            return func(arg)
        return wrapper
    return decor


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plot_signal(signal)