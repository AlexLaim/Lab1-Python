lst = [2, 3, 5, 20, 100]

for i in range(len(lst)):
    if i != (len(lst) - 1) and lst[i] > lst[i+1]:
        print("False")
        break
    elif i == (len(lst) - 1):
        print("True")
