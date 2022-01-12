class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __average_grade (self):
        amount_grades = 0
        for course in self.grades.values():
            for number in course:
                amount_grades += number
        all_grades = 0
        for course in self.grades.values():
            all_grades += len(course)
        return ("{0:.1f}".format(amount_grades / all_grades))
    def __str__(self):
        res = f' {self.name} {self.surname} {self.__average_grade()} {self.courses_in_progress} {self.finished_courses}'
        return res
    def __lt__(self,other):
        if not isinstance(other,Student):
            print('Not a Student')
            return
        res = self.__average_grade() < other.__average_grade ()
        return res
        
    def rating (self, lector, course, grade):
        if isinstance(lector, Lectcurer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Error'             
class Mentors:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        courses_attached =[]
class Lectcurer(Mentors):
    def __init__(self, name, surname):
       super().__init__(name,surname)
       self.courses_attached =[]
       self.grades = {}
    def __average_grade (self):
        amount_grades = 0
        for course in self.grades.values():
            for number in course:
                amount_grades += number
        all_grades = 0
        for course in self.grades.values():
            all_grades += len(course)
        return ("{0:.1f}".format(amount_grades / all_grades))
    def __lt__(self,other):
        if not isinstance(other,Lectcurer):
            print('Not a Lectcurer')
        res = self.__average_grade < other.__average_grade
        return res

    def __str__(self):
        res = f' {self.name} {self.surname} {self.__average_grade()}'
        return res
class Reviewer(Mentors):
    def __init__(self, name, surname):
       super().__init__(name,surname)
       self.courses_attached =[]
    def put_a_rating(self,student,course,grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else :
                student.grades[course] = [grade]
        else:
            print('Error')
    def __str__(self):
        res = f' {self.name} {self.surname}'
        return res
def aver_grad_cour_stud (students,name_course):
    for student in students:
        if name_course in student.grades.keys():
            all_grades = 0
            amount_grades = 0
            for grade in student.grades[name_course]:
                amount_grades += grade
            aver_grad_cour = amount_grades / (len(student.grades[name_course]))
            print(f' Средняя оценка студента по имени {student.name} по курсу {name_course} {aver_grad_cour}')
        else:
            print (f'Студент по имени {student.name} по курс {name_course} не изучает')       
def aver_grad_cour_lect (lectors,name_course):
    for lector in lectors:
        if name_course in lector.grades.keys():
            all_grades = 0
            amount_grades = 0
            for grade in lector.grades[name_course]:
                amount_grades += grade
            aver_grad_cour = amount_grades / (len(lector.grades[name_course]))
            print(f' Средняя оценка лектора по имени {lector.name} по курсу {name_course} {aver_grad_cour}')
        else:
            print (f'Лектор по имени {lector.name} по курс {name_course} не преподает')