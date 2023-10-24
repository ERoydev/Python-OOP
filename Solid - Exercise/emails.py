from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MaskedContent(IContent):
    def format(self):
        return '*' * len(self.text)


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content.format())


class MyContent(IContent):
    def format(self):
        return '<myML>\n' + self.text + '\n' + '</myML>'


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(MyContent("Hello there!"))
print(email)