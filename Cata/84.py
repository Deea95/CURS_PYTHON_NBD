a =[5, 2, 8, 4, 6, 22, 8, 9] 
m = 15 
c = '#' 
t = '' 
max_value = 0 
n = len(a) 
for i in range(n):
    if a[i]> max_value:
        max_value = a[i]
for i in range(n): 
            f = int((m / max_value)* a[i]) 
            for k in range(f): 
                t += c 
            t += '\n' 
print(t)