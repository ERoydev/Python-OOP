
def number_increment(numbers):
    def increase():
        res = [i+1 for i in numbers]
        return res

    return increase()


print(number_increment([1, 2, 3]))