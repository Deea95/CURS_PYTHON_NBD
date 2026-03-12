# This example creates an object
# with three properties. The cx
# property is a method.
class MyObject:
    def __init__(self):
        def cx(self, g):
            t = self.ax + g + str(len(self
            # Create an instance
            # of the class.
            obj = MyObject()
            # Use the functions and
            # properties of the object.
            print(obj.cx("-"))
            print(obj.ax)
            print(obj.bx)
            # Modify the properties.
            # Print the modified
            # properties and the result
            # of the function.
            print(obj.ax)
            print(obj.bx)
            print(obj.cx("+"))