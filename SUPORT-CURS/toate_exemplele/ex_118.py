# 7.1.24 Ex. (118) – Add two matrices into a third
a = [Output:
[2, 4, 6],
[3, 5, 6], 4
8
12
[3, 5, 4]
6
10
12
]                               6
10
8
b = [
    [2, 4, 6], '''                     
            [3, 5, 6],                    for substraction:       
            [3, 5, 4]                                             
            ]                             0 0 0                   
          c = []                          0 0 0                   
          r = ""                                                  
          for i in range(len(a)):                                 
            r += "\n"                                             
            c.append([])                                          
            for j in range(len(a[i])):                            
               c[i].append(a[i][j] + b[i][j])                     
               r += str(c[i][j]) + " "                            
          print(r)                                                
          # or a second version:                                  
          a = [                                                   
            [2, 4, 6],                                            
            [3, 5, 6],                                            
            [3, 5, 4]                                             
            ]                                                     
          b = [                                                   
            [2, 4, 6],                                            
            [3, 5, 6],                                            
            [3, 5, 4]                                             
            ]                                                     
          # Pre-allocate the size of c.                           
          c = [[0] * len(a[0]) for _ in range(len(a))]            
          r = ""                                                  
          for i in range(len(a)):                                 
            r += "\n"                                             
            for j in range(len(a[i])):                            
               c[i][j] = a[i][j] + b[i][j]                        
               r += str(c[i][j]) + " "                            
          print(r)
