

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget and self.__animal_capacity > 0:
            return "Not enough budget"

        elif self.__animal_capacity <= 0:
            return "Not enough space for animal"

        animal_type = animal.__class__.__name__
        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {animal_type} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker):
        for human in self.workers:
            if human.name == worker:
                self.workers.remove(human)
                return f"{worker} fired successfully"

        return f"There is no {worker} in the zoo"

    def pay_workers(self):
        total_money_to_pay_all_workers = sum([x.salary for x in self.workers])
        if total_money_to_pay_all_workers > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_money_to_pay_all_workers
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_to_tend_all_animals = sum([x.money_for_care for x in self.animals])
        if total_money_to_tend_all_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_money_to_tend_all_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_animals_str('Lion', self.animals)
        result += self.__build_animals_str('Tiger', self.animals)
        result += self.__build_animals_str('Cheetah', self.animals)
        return result.rstrip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        result += self.__build_animals_str('Keeper', self.workers)
        result += self.__build_animals_str('Caretaker', self.workers)
        result += self.__build_animals_str('Vet', self.workers)
        return result.rstrip()

    def __build_animals_str(self, info_type, collection): #Helper method nai dolu
        counter = 0
        result = ''
        for animal in collection:
            if animal.__class__.__name__ == info_type:
                counter += 1
                result += repr(animal) + "\n"

        return f"----- {counter} {info_type}s:\n" + result
