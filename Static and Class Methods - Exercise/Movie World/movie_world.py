
class MovieWorld:
    def __init__(self, name: str, ):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = MovieWorld.__find_obj_by_id(customer_id, self.customers)
        dvd = MovieWorld.__find_obj_by_id(dvd_id, self.dvds)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = MovieWorld.__find_obj_by_id(customer_id, self.customers)
        dvd = MovieWorld.__find_obj_by_id(dvd_id, self.dvds)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        output = []
        MovieWorld.__print_data(self.customers, output)
        MovieWorld.__print_data(self.dvds, output)
        return '\n'.join(output)


    @staticmethod
    def __print_data(collection, output):
        for i in collection:
            output.append(f"{str(i)}")

    @staticmethod
    def __find_obj_by_id(id, collection):
        for obj in collection:
            if obj.id == id:
                return obj
