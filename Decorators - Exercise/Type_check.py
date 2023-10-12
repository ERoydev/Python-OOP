
def type_check(type):
    def decorator(func_ref):
        def wrapper(parameter):
            if not isinstance(parameter, type):
                return "Bad Type"

            func_result = func_ref(parameter)
            return func_result

        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))


