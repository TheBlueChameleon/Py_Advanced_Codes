class Monoid (int) :
    def __init__ (self, arg = 0) :
        #super().__init__(arg)
        self.x = arg
        
    def __matmul__(self, rhs) :
        return self


def makeMonoid(f) :
    def inner(*args, **kwargs) :
        return Monoid(f(*args, **kwargs))
    return inner

m = Monoid(5)

print(m.__add__(5))
print(type(m.__add__(5)))
print()

m.__add__ = makeMonoid(m.__add__)

print(m.__add__(5))
print(type(m.__add__(5)))
print(type(m + 5))
print()