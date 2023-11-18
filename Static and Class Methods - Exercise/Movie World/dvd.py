import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date: str, age_restriction):
        data = [int(x) for x in date.split('.')[1:]]
        month, year = calendar.month_name[data[0]], data[1]
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")









