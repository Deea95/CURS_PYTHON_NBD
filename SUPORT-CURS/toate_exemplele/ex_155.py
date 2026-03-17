# 9.1.3 Ex. (155) – An object with three properties and a method (II)
# This example creates an object   Output:
# with three properties. The cx
# property is a method.            this-4
def __init__(self):             super


self.ax = "this"
self.bx = "text"


def cx(self, g):
    t = self.ax + g + str(len(self.bx))
    return t
    # Create an instance
# of the class.
obj = MyObject()
# Use the functions and
# properties of the object.
print(obj.cx("-"))
print(obj.ax)
print(obj.bx)
# Modify the properties.
obj.ax = "super"
obj.bx = "string"
# Print the modified
# properties and the result
# of the function.
print(obj.ax)
print(obj.bx)
print(obj.cx("+"))
