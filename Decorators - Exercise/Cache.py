
def cache(func_ref):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]

        func_res = func_ref(number)
        log[number] = func_res
        return func_res

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n

    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
