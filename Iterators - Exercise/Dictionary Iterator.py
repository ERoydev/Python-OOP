
class dictionary_iter:

    def __init__(self, obj):
        self.obj = obj
        self.index = 0
        self.end = len(obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration()

        key = list(self.obj)[self.index]
        self.index += 1
        return key, self.obj[key]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


