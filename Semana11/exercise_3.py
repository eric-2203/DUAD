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


def get_student_info():
    global details
    global average
    global all_scores
    
    average = []
    all_scores = []

    name = input("Student name: ")
    section = input("Section: ")
    spanish_score = int(input("Spanish Score: "))
    english_score = int(input("English Score: "))
    science_score = int(input("Science Score: "))
    socials_score = int(input("Socials Score: "))
    details = [name, section, spanish_score, english_score, science_score, socials_score]
    average_scores = (spanish_score + english_score + science_score + socials_score)/4

    top_students = average_scores

    all_scores.append(spanish_score)
    all_scores.append(english_score)
    all_scores.append(science_score)
    all_scores.append(socials_score)

    ranking = [name, top_students]
    average.append(ranking)


    return Student


def register_student():
    global students
    students = []

    while True:
        student = get_student_info()
        students.append(details)

        
        more_info = input("Do you want to add more students information? (yes/no): ")
        if more_info.lower() != 'yes':
            break
        
    return students

def show_top_3():
    sorted_average = sorted(average, key=lambda scores: scores[1], reverse=True)
    top_3 = sorted_average[:3]

    print(f'These are the top 3 students with their average score: {top_3}')



register_student()
print(students)
show_top_3()