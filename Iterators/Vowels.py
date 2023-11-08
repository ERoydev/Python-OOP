
class vowels:
    def __init__(self, obj):
        self.obj = obj
        self.i = 0
        self.end = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current = self.obj[self.i]
            self.i += 1

            if current.lower() in "auoyei":
                return current

        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')

for char in my_string:
    print(char)
