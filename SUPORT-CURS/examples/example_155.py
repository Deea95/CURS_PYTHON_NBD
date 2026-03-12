             def __init__(self):
               self.ax = "this"
               self.bx = "text"
             def cx(self, g):
               t = self.ax + g + str(len(self
          obj = MyObject()
          print(obj.cx("-"))
          print(obj.ax)
          print(obj.bx)
          obj.ax = "super"
          obj.bx = "string"
          print(obj.ax)
          print(obj.bx)
          print(obj.cx("+"))
        the bx property from “text” to “string.” (f)
        updated value for the ax property, which is n