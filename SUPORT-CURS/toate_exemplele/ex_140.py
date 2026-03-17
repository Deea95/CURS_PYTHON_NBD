def compute(x):                    
    return x + x / x - x * x

def distribution(start, stop):     
    t = ""
    for i in range(start, stop):    
        t += str(compute(i)) + "\n"
    return t

a = distribution(3, 21)
print(a)