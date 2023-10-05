
class Task:

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comment = []
        self.completed = False

    def change_name(self, new_name):
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_date):
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date

        return "Date cannot be the same."

    def add_comment(self, comment):
        self.comment.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < 0 or comment_number > len(self.comment)-1:
            return f"Cannot find comment."

        self.comment[comment_number] = new_comment
        return ', '.join(self.comment)

    def details(self):
        return f"Name: {self.name} - Due_date: {self.due_date}"
