
def vowel_filter(function):

    def wrapper():
        result = function()
        return [el for el in result if el.lower() in "aeiuy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

@vowel_filter
def another_letters():
    return ['e','s','h']


print(get_letters())
print(another_letters())
