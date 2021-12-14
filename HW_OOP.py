class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def grade_average(self):
        sum_g = 0
        len_g = 0
        for key in self.grades:
            sum_g = sum_g + sum(self.grades[key])
            len_g = len_g + len(self.grades[key])
        average = round(sum_g / len_g, 2)
        return average
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grade_average()}\n' \
              f'Курсы в процессе изучения: { "," .join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {"," .join(self.finished_courses)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.grade_average() < other.grade_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def grade_average(self):
        sum_g = 0
        len_g = 0
        for key in self.grades:
            sum_g = sum_g + sum(self.grades[key])
            len_g = len_g + len(self.grades[key])
        average = round(sum_g / len_g, 2)
        return average
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grade_average()}\n'
        return res
    def __lt__ (self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.grade_average() < other.grade_average()

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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

student_ivan = Student('Ivan', 'Ivanov', 'male')
student_ivan.finished_courses += ['Java']
student_ivan.courses_in_progress += ['Python', 'Git']

student_alina = Student('Alina', 'Sidorova', 'female')
student_alina.finished_courses += ['Введение в программирование']
student_alina.courses_in_progress += ['Java', 'Git', 'Python']

lecturer_petrov = Lecturer('Petr', 'Petrov')
lecturer_petrov.courses_attached += ['Python','Git']

lecturer_vetrov = Lecturer('Anton', 'Vetrov')
lecturer_vetrov.courses_attached += ['Python','Git']

reviewer_smolov = Reviewer('Fedor', 'Smolov')
reviewer_smolov.courses_attached += ['Java', 'Python']

reviewer_petrov = Reviewer('Petr', 'Petrov')
reviewer_petrov.courses_attached += ['Git', 'Python']

reviewer_smolov.rate_hw(student_ivan, 'Python', 5)
reviewer_smolov.rate_hw(student_ivan, 'Python', 5)
reviewer_smolov.rate_hw(student_ivan, 'Python', 5)

reviewer_petrov.rate_hw(student_ivan, 'Git', 5)
reviewer_petrov.rate_hw(student_ivan, 'Git', 5)
reviewer_petrov.rate_hw(student_ivan, 'Git', 5)

reviewer_petrov.rate_hw(student_alina, 'Git', 10)
reviewer_petrov.rate_hw(student_alina, 'Git', 10)
reviewer_petrov.rate_hw(student_alina, 'Git', 10)

reviewer_smolov.rate_hw(student_alina, 'Python', 10)
reviewer_smolov.rate_hw(student_alina, 'Python', 10)
reviewer_smolov.rate_hw(student_alina, 'Python', 10)

student_ivan.rate_lecturer(lecturer_petrov, 'Git', 5)
student_ivan.rate_lecturer(lecturer_petrov, 'Git', 10)

student_ivan.rate_lecturer(lecturer_vetrov, 'Python', 5)
student_ivan.rate_lecturer(lecturer_vetrov, 'Python', 10)

student_alina.rate_lecturer(lecturer_petrov, 'Python', 7)
student_alina.rate_lecturer(lecturer_petrov, 'Python', 7)

print(f'Студент Иван Иванов\n{student_ivan}\n')
print(f'Студент Алина Сидорова\n{student_alina}\n')
print(f'Лектор Петр Петров\n{lecturer_petrov}\n')
print(f'Лектор Антон Ветров\n{lecturer_vetrov}\n')

print('У Петрова средняя оценка за лекции больше, чем у Ветрова:', lecturer_petrov>lecturer_vetrov)
print('У Иванова средняя оценка за ДЗ больше, чем у Сидоровой:', student_ivan>student_alina)

list_st = [student_ivan, student_alina]
list_lec = [lecturer_petrov, lecturer_vetrov]
def student_average_course(list_st, course):
    list_grade = []
    for student in list_st:
        list_grade += student.grades[course]
    average_course = sum(list_grade)/len(list_grade)
    return average_course
print('\nСредняя оценка за ДЗ по курсу Git:', student_average_course(list_st,'Git'))
def lecturer_average_course(list_lec, course):
    list_grade_lec = []
    for lecturer in list_lec:
        list_grade_lec += lecturer.grades[course]
    average_course_lec = sum(list_grade_lec)/len(list_grade_lec)
    return average_course_lec
print('\nСредняя оценка за лекции по курсу Python:', lecturer_average_course(list_lec,'Python'))