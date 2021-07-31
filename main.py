class Student:
    registry = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.registry.append(self)

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_number(self):
        for i in self.grades.values():
            average = sum(i) / len(i)
            return average

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_number()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    registry = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.registry.append(self)

    def average_number(self):
        for i in self.grades.values():
            average = sum(i) / len(i)
            return average

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_number()}"
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}"
        return result

value = 0
name = ''
value1 = 0
name1 = ''
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'java']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

best_lecturer = Lecturer("Pavel", "Pavlovich")
best_lecturer.courses_attached += ['java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_hw(best_lecturer, 'java', 10)
best_student.rate_hw(best_lecturer, 'java', 8)
best_student.rate_hw(best_lecturer, 'java', 6)

ordinary_student = Student('Lola', 'Lolovna', 'your_gender')
ordinary_student.courses_in_progress += ['Python', 'java']
cool_reviewer.rate_hw(ordinary_student, 'Python', 3)
cool_reviewer.rate_hw(ordinary_student, 'Python', 5)
cool_reviewer.rate_hw(ordinary_student, 'Python', 7)

print(f"{cool_reviewer}\n\n{best_lecturer}\n\n{best_student}")

for students in Student.registry:
    if students.average_number() > value:
        value = students.average_number()
        name = students.name

for lecturer in Lecturer.registry:
    if lecturer.average_number() > value1:
        value1 = lecturer.average_number()
        name1 = lecturer.name
print(f"Лучший студент: {name} с средним баллом по д/з: {value}")
print(f"Лучший лектор: {name1} с средним баллом по лекциям: {value1}")