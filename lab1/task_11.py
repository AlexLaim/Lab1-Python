def frange(start, end, step):
    while start < end:  
        yield round(start,1)
        start += step
        

for i in frange(1, 5, 0.1):
    print(i)