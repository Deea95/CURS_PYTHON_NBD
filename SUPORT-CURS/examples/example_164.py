          txt = '{"v1":["a","b","c"],"v2":' + \
              '[[0,1,0],[1,1,1],[0,1,0]]' + \
              ',"v3":{"c1":["a","b","c"]' + \
              ',"c2":[[0,1,0],[1,1,1],[0' + \
              ',1,0]],"c3":42}}'
          obj = json.loads(txt)
          a = []
          for i in range(len(obj['v3']['c2'])):
             a.append([])
             for j in range(len(obj['v3']['c2']
               a[i].append(obj['v3']['c2'][i]
          def smc(m):
             r = ''
             for i in range(len(m)):
               for j in range(len(m[i])):
                  r += str(m[i][j]) + " "
               r += "\n"
          print(smc(a))
        found inside a complex object (obj). A strin
        (i.e. points i–vi). The code then parses the J
        for each element, it initializes a sub-array in a
        takes a matrix (m) as an argument. Inside
        turn prints the matrix to the console.
        valuable teaching tools for both beginners
        for those eager to deepen their understanding