            def SMC(matrix):
              result = ""
              for row in matrix:
                for item in row:
                   result += item + " "
                result += "\n"
            c = 'AAAAA|BBBBB|CCCCC|DDDDD'
            n = c.split('|')
            m = [list(row) for row in n]
            print(SMC(m))
                     c = “AAAAA|BBBB
          Then c is split into parts using the split(