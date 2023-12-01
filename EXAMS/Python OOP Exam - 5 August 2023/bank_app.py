from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.adult import Adult
from project.clients.student import Student


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in BankApp.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return f"Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        # Take first loan type --------- possible mistake
        loan = self._find_loan_by_type(loan_type)
        client = self._find_client_by_id(client_id)

        if loan.TYPE != client.LOAN_TYPE:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        loan.loan_change_granted_status()
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = self._find_client_by_id(client_id)
        if not client:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        filtered = [loan for loan in self.loans if loan.TYPE == loan_type and not loan.granted]
        [x.increase_interest_rate() for x in filtered]

        return f"Successfully changed {len(filtered)} loans."

    def increase_clients_interest(self, min_rate):
        filtered = [client for client in self.clients if client.interest < min_rate]
        [x.increase_clients_interest() for x in filtered]

        return f"Number of clients affected: {len(filtered)}."

    def get_statistics(self):
        granted_to_clients, granted_sum = self._get_granted_and_sum_of_loans()
        not_granted, not_granted_sum = self._get_available_loans()
        average_client_rate = self._get_average_clients_rate()

        output = f'Active Clients: {len(self.clients)}'
        output += f"\nTotal Income: {sum([x.income for x in self.clients]):.2f}"
        output += f"\nGranted Loans: {granted_to_clients}, Total Sum: {granted_sum:.2f}"
        output += f"\nAvailable Loans: {not_granted}, Total Sum: {not_granted_sum:.2f}"
        output += f'\nAverage Client Interest Rate: {average_client_rate:.2f}'

        return output

    # HELPER METHODS
    def _get_average_clients_rate(self):
        result = 0
        if len(self.clients) > 0:
            result = sum([x.interest for x in self.clients]) / len(self.clients)

        return result

    def _get_available_loans(self):
        count, total_sum = 0, 0
        for loan in self.loans:
            if not loan.granted:
                count += 1
                total_sum += loan.amount

        return count, total_sum

    def _get_granted_and_sum_of_loans(self):
        count = 0
        total_sum = 0
        for client in self.clients:
            count += len(client.loans)
            total_sum += sum([x.amount for x in client.loans])

        return count, total_sum

    def _find_loan_by_type(self, loan_type):
        for loan in self.loans:
            if loan.TYPE == loan_type:
                return loan

    def _find_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
