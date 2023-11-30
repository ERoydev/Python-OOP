from abc import ABC, abstractmethod


class FileRule(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def execute(self):
        pass


class HeaderRule(FileRule):
    columns = ['name', 'age']

    def execute(self):
        # open file, gather all columns and check them
        if self.file.columns != self.columns:
            raise Exception('Columns are missing')


class CharRule(FileRule):
    def execute(self):
        pass

class DigitRule(FileRule):
    def execute(self):
        # check if every age is digit
        for age in self.file['age']:
            pass


class Invoker:
    def __init__(self, file):
        self.file = file
        self._commands = []

    def store_commands(self, command):
        self._commands.append(command(self.file))

    def execute_command(self):
        for command in self._commands:
            command.execute()


i = Invoker('asd.txt')
i.store_commands(HeaderRule)
i.store_commands(CharRule)
i.store_commands(DigitRule)

i.execute_command()