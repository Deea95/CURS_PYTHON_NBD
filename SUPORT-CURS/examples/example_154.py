# This example creates an
# object with three properties.
# The cx property is a method.
class Obj:
    def __init__(self):
        def cx(self):
            # Create an instance of the
            # Obj class and call the cx method.
            obj = Obj()
            print(obj.cx())