class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._index = 0  # To keep track of iteration state

    def __iter__(self):
        self._index = 0  # Reset the iteration every time a new loop starts
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {"length": self.length}
        elif self._index == 1:
            self._index += 1
            return {"width": self.width}
        else:
            raise StopIteration


rect = Rectangle(5, 10)

for info in rect:
    print(info)
