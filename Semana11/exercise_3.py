import csv

class Student():
    def __init__(self, name, section, score1, score2, score3, score4):
        self.name = name
        self.section = section
        self.spanish = score1
        self.english = score2
        self.science = score3
        self.socials = score4
        self.details = self.name, self.section, self.spanish, self.english, self.science, self.socials
        self.average = (self.spanish + self.english + self.science + self.socials)/4
        

    def show_details(self):
        print(f"Student's name: {self.name}, Section: {self.section}, Spanish Score: {self.spanish}, English Score: {self.english}, Science Score: {self.science}, Socials Score: {self.socials}")

    def get_average(self):
        self.average = (self.spanish + self.english + self.science + self.socials) / 4
        print(f"Average score: {self.average}")

name = input("Student name: ")
section = input("Section: ")
spanish_score = int(input("Spanish Score: "))
english_score = int(input("English Score: "))
science_score = int(input("Science Score: "))
socials_score = int(input("Socials Score: "))

students_list = []
while True:
    students = Student(name, section, spanish_score, english_score, science_score, socials_score)
    students_list.append(students)
    more_info = input("Do you want to add more students information? (yes/no): ")
    if more_info.lower() != 'yes':
        break


students.show_details()