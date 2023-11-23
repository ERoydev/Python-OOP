def cache(func):
    def wrapper(n):
        if not wrapper.log.get(n):
            wrapper.log[n] = func(n)

        return wrapper.log.get(n)

    wrapper.log = {}

    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

