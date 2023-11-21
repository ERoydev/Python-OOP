
class countdown_iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == -1:
            raise StopIteration

        temp = self.count
        self.count -= 1
        return temp


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")