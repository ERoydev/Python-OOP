from project.clients.base_client import BaseClient


class Adult(BaseClient):
    LOAN_TYPE = "MortgageLoan"
    INITIAL_INTEREST = 4
    INCREASE_INTEREST = 2

    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, Adult.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += Adult.INCREASE_INTEREST
