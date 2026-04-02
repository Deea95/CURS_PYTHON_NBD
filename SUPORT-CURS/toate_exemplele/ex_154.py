# 9.1.2 Ex. (154) – An object with three properties and a method (I)
# This example creates an
# object with three properties.
# The cx property is a method.
class Obj:
    def __init__(self):
        self.ax = "this"
        self.bx = "text"

    def cx(self):
        return self.ax + " " + self.bx
    # Create an instance of the
# Obj class and call the cx method.
obj = Obj()
print(obj.cx())
