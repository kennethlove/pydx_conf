class Add:
    def __init__(self, default=0):
        self.default = default

    def __call__(self, extra=0):
        return self.default + extra


add2 = Add(2)
print(add2(3))
