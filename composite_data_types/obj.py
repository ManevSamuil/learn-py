# Example of using object methods
class MyDerivedClass(object):
    def __init__(self, value):
        self.value = value

obj = MyDerivedClass(42)
print(obj.value)  # Output: 42
