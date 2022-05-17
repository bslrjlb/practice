from fnmatch import fnmatch


class Function:
    def __init__(self, fn):
        self.function = fn

    def __call__(self, x):
        self.function = fn
        return fn(x)

class CentralDifferenceFunction(Function):
    def __init__(self, fn, delta):
        self.function = fn
        self.selta = delta

    def derivative(self, x, delta=None):


class Exception(Function):


class ConvergenceError(Function):

