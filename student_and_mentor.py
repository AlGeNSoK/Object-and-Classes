class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_hw(self):
        if self.grades:
            average_grade_hw_list = sum(self.grades.values(), start=[])
            result = round(sum(average_grade_hw_list) / len(average_grade_hw_list), 1)
        else:
            result = "Нет оценок"
        return result

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade_hw()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if self.average_grade_hw() == "Нет оценок" or other.average_grade_hw() == "Нет оценок":
            result = "У студента (студентов) нет оценок за лекции!"
        else:
            result = self.average_grade_hw() < other.average_grade_hw()
        return result


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade_lectur(self):
        if self.grades:
            average_grade_lectur_list = sum(self.grades.values(), start=[])
            result = round(sum(average_grade_lectur_list) / len(average_grade_lectur_list), 1)
        else:
            result = "Нет оценок"
        return result

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade_lectur()}")

    def __lt__(self, other):
        if self.average_grade_lectur() == "Нет оценок" or other.average_grade_lectur() == "Нет оценок":
            result = "У лектора (лекторов) нет оценок за лекции!"
        else:
            result = self.average_grade_lectur() < other.average_grade_lectur()
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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Sam', 'Carter', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

super_lecturer = Lecturer('Bill', 'Smith')
super_lecturer.courses_attached += ['Python']

lecturer_git = Lecturer('John', 'Brown')
lecturer_git.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 8)

cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 9)

print(best_student.grades)
print(second_student.grades)
print()

best_student.rate_lectures(super_lecturer, 'Python', 10)
best_student.rate_lectures(super_lecturer, 'Python', 10)
best_student.rate_lectures(super_lecturer, 'Python', 7)
best_student.rate_lectures(lecturer_git, 'Git', 10)
best_student.rate_lectures(lecturer_git, 'Git', 10)
best_student.rate_lectures(lecturer_git, 'Git', 10)

print(super_lecturer.grades)
print()

print(cool_reviewer)
print()
print(super_lecturer)
print()
print(best_student)
print()

print(best_student > second_student)
print(super_lecturer > lecturer_git)