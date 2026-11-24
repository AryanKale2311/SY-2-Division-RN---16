
def uppercase(func):
    def wrapper(self):
        return func(self).upper()
    return wrapper


class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def create_report(cls, title, content):
        return cls(title, content)

    @uppercase
    def generate(self):
        return self.title + "\n" + self.content

    def __str__(self):
        return "Report: " + self.title


r1 = Report.create_report("Student Report", "Name: Aryan\nMarks: 90")

print(r1)
print(r1.generate())
