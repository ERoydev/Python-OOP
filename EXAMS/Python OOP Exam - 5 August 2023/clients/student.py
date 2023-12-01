from project.clients.base_client import BaseClient


class Student(BaseClient):
    LOAN_TYPE = "StudentLoan"
    INITIAL_INTEREST = 2
    INCREASE_INTEREST = 1.0

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, Student.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += Student.INCREASE_INTEREST
