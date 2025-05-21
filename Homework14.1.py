class TooManyStudentsError(Exception):
    def __init__(self, message="There cannot be more than 10 students in a group"):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group: {self.number}\n{all_students}"

gr = Group('PD1')

for i in range(10):
    s = Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'AN14{i}')
    gr.add_student(s)

print(gr)

try:
    extra_student = Student('Male', 25, 'John', 'Doe', 'AN999')
    gr.add_student(extra_student)
except TooManyStudentsError as e:
    print("Error:", e)