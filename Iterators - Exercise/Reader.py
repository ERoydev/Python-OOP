

def read_next(*args):
    idx = 0
    for element in args:
        for i in element:
            yield i


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')