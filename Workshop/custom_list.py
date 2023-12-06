from typing import Any, Optional, Iterable, Dict, List
from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value) -> List[Any]:
        self.__values.append(value)
        return self.__values

    def remove(self, index) -> List[Any]:
        if len(self.__values)-1 < index:
            raise IndexError('List index out of range')

        return self.__values.pop(index)

    def get(self, index):
        if len(self.__values)-1 < index:
            raise IndexError('List index out of range')

        return self.__values[index]

    def extend(self, value, *args):
        if isinstance(value, Iterable):
            self.__values.extend(value)

        else:
            self.__values.append(value)

        self.__values.extend(args)
        return self.__values

    def insert(self, index, value):
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        return self.__values.pop()

    def clear(self):
        self.__values = []

    def index(self, value):
        result = None
        try:
            result = self.__values.index(value)
        except ValueError:
            result = f'{value} is not in list'
        return result

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)

    def dictionize(self) -> Dict[Any, Any]:
        result = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]
            try:
                value = self.__values[index + 1]
            except IndexError:
                value = " "

            result[key] = value
        return result

    def move(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Amount should be integer!')

        if amount < 0:
            raise ValueError('Cannot move a negative amount!')

        if amount > len(self.__values):
            return self.__values

        self.__values = self.__values[amount:] + self.__values[0:amount]
        return self.__values

    def sum(self):
        result = 0
        for value in self.__values:
            if isinstance(value, int) or isinstance(value, float):
                result += value
            else:
                result += len(value)

        return result

    def overbound(self):
        max_number = float('-inf')
        for value in self.__values:
            result = 0
            if isinstance(value, int) or isinstance(value, float):
                result = value
            else:
                result = len(value)
            if result > max_number:
                max_number = result
        return max_number

    def underbound(self):
        min_number = float('inf')
        for value in self.__values:
            result = 0
            if isinstance(value, int) or isinstance(value, float):
                result = value
            else:
                result = len(value)
            if result < min_number:
                min_number = result

        return min_number