

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [subs for subs in self.subscriptions if subs.id == subscription_id][0]
        output = f"{str(subscription)}\n"
        output += self.__get_data_for_output(self.customers, subscription.customer_id)
        output += self.__get_data_for_output(self.trainers, subscription.trainer_id)
        output += self.__get_data_for_output(self.equipment, subscription.exercise_id)
        output += self.__get_data_for_output(self.plans, subscription.exercise_id)
        return output
    

    def __get_data_for_output(self, collection, id):
        for obj in collection:
            if obj.id == id:
                return str(obj) + "\n"


