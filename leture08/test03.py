#OOP
#Camel case , Snake case
class DtiSau :
    student_name = ' '
    score = 0
    gpa = 0

    def hisStudent(self):
        print(f'สวัสดี {self.student_name}')

    def showScorAndGrade(self):
        print(f'คะแนน {self.score} ได้เกรด {self.gpa}')

obj01 = DtiSau()
obj02 = DtiSau()

obj01.student_name = 'สมชาย'
obj01.hisStudent()
obj02.score = 99
obj02.gpa = 3.99