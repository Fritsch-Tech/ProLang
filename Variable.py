class Variable :
    def __init__(self, name: str, value) :
        self.name = name
        self.value = int(value)

    def __str__(self) :
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __call__(self):
        return self.__str__()
