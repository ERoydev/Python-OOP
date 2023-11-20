from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    VEHICLE_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._find_user_by_driving_license(driving_license_number) is not None:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._find_vehicle_by_license_number(license_plate_number) is not None:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = ManagingApp.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self._find_route_by_start_end_points(start_point, end_point)

        if route is not None:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = self._find_user_by_driving_license(driving_license_number)
        vehicle = self._find_vehicle_by_license_number(license_plate_number)
        route = self._find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [x for x in self.vehicles if x.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key= lambda x: (x.brand, x.model))[:count]
        for vehicle in selected_vehicles:
            vehicle.change_status()
            vehicle.recharge()

        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        output = ['*** E-Drive-Rent ***', ]
        for user in sorted(self.users, key=lambda x: -x.rating):
            output.append(str(user))

        return '\n'.join(output)

    # HELPER METHODS

    def _find_route_by_id(self, route_id):
        filtered_routes = [route for route in self.routes if route.route_id == route_id]

        if filtered_routes:
            return filtered_routes[0]
        return None

    def _find_vehicle_by_license_number(self, license_number):
        filtered_vehicles = [vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_number]

        if filtered_vehicles:
            return filtered_vehicles[0]
        return None

    def _find_user_by_driving_license(self, driving_license):
        filtered_users = [user for user in self.users if user.driving_license_number == driving_license]
        if filtered_users:
            return filtered_users[0]
        return None

    def _find_route_by_start_end_points(self, startpoint, endpoint):
        filtered_routes = [route for route in self.routes if route.start_point == startpoint and route.end_point == endpoint]

        if filtered_routes:
            return filtered_routes[0]
        return None


