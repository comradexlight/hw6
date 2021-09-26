class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = 0

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_middle_grade(self):
        rate = 0
        count = 0
        for i in self.grades.values():
            for point in i:
                rate += point
                count += 1
        self.middle_grade = round(rate / count, 1)
        return self.middle_grade

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не явдяется студеннтом')
            return
        return self.middle_grade < other.middle_grade

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.middle_grade}'\
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.middle_rate = 0

    def get_middle_rate(self):
        rate = 0
        count = 0
        for i in self.grades.values():
            for point in i:
                rate += point
                count += 1
        self.middle_rate = round(rate / count, 1)
        return self.middle_rate

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_rate}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не явдяется лектором')
            return
        return self.middle_rate < other.middle_rate

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
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



alex_thestudent = Student('Alex', 'Smirnov', 'male')
victoria_thestudent = Student('Victoria', 'Ivanova', 'female')

olga_thelecturer = Lecturer('Olga', 'Simakova')
vladimir_thelecturer = Lecturer('Vladimir', 'Osipov')

sveta_thereviewer = Reviewer('Svetlana', 'Bykova')
denis_thereviewer = Reviewer('Denis', 'Alekseev')

alex_thestudent.courses_in_progress += ['Python']
alex_thestudent.courses_in_progress += ['Git']
alex_thestudent.finished_courses += ['Введение в программирование']

victoria_thestudent.courses_in_progress += ['Python']
victoria_thestudent.courses_in_progress += ['Git']
victoria_thestudent.finished_courses += ['Введение в программирование']
victoria_thestudent.finished_courses += ['Scrum']

olga_thelecturer.courses_attached += ['Python']

vladimir_thelecturer.courses_attached += ['Git']

sveta_thereviewer.courses_attached += ['Python']
sveta_thereviewer.courses_attached += ['Git']

denis_thereviewer.courses_attached += ['Python']
denis_thereviewer.courses_attached += ['Git']


sveta_thereviewer.rate_hw(alex_thestudent, 'Python', 10)
sveta_thereviewer.rate_hw(alex_thestudent, 'Python', 6)
denis_thereviewer.rate_hw(alex_thestudent, 'Python', 8)
denis_thereviewer.rate_hw(alex_thestudent, 'Git', 10)
denis_thereviewer.rate_hw(alex_thestudent, 'Git', 7)
sveta_thereviewer.rate_hw(alex_thestudent, 'Git', 10)

sveta_thereviewer.rate_hw(victoria_thestudent, 'Python', 8)
denis_thereviewer.rate_hw(victoria_thestudent, 'Python', 8)
denis_thereviewer.rate_hw(victoria_thestudent, 'Python', 7)
sveta_thereviewer.rate_hw(victoria_thestudent, 'Git', 10)
sveta_thereviewer.rate_hw(victoria_thestudent, 'Git', 6)
denis_thereviewer.rate_hw(victoria_thestudent, 'Git', 9)

alex_thestudent.rate_lection(olga_thelecturer, 'Python', 10)
alex_thestudent.rate_lection(olga_thelecturer, 'Python', 8)
alex_thestudent.rate_lection(vladimir_thelecturer, 'Git', 10)

victoria_thestudent.rate_lection(olga_thelecturer, 'Python', 7)
victoria_thestudent.rate_lection(vladimir_thelecturer, 'Git', 10)
victoria_thestudent.rate_lection(vladimir_thelecturer, 'Git', 6)

alex_thestudent.get_middle_grade()
victoria_thestudent.get_middle_grade()

olga_thelecturer.get_middle_rate()
vladimir_thelecturer.get_middle_rate()

print(alex_thestudent)
print(victoria_thestudent)
print(olga_thelecturer)
print(vladimir_thelecturer)
print(denis_thereviewer)
print(sveta_thereviewer)

print(alex_thestudent > victoria_thestudent)
print(olga_thelecturer > vladimir_thelecturer)

group_one = [alex_thestudent, victoria_thestudent]
group_two = [vladimir_thelecturer, olga_thelecturer]


def middle_rate_of_students(list_of_srudents, course_name):
    rate = 0
    count = 0
    for student in list_of_srudents:
        for k,v in student.grades.items():
            if course_name == k:
                for point in v:
                    rate += point
                    count += 1
    mid_rate = round(rate / len(list_of_srudents) / count, 1)
    print(f'Cредняя оценка за домашние задания по всем студентам в рамках курса по {course_name} равна {mid_rate}')
    return mid_rate

def middle_rate_of_lecturers(list_of_lecturers, course_name):
    rate = 0
    count = 0
    for lecturer in list_of_lecturers:
        for k,v in lecturer.grades.items():
            if course_name == k:
                for point in v:
                    rate += point
                    count += 1
    mid_rate = round(rate / len(list_of_lecturers) / count, 1)
    print(f'Cредняя оценка за лекции всех лекторов в рамках курса по {course_name} равна {mid_rate}')
    return mid_rate

middle_rate_of_students(group_one, 'Python')
middle_rate_of_lecturers(group_two, 'Git')