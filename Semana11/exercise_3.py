import csv

class Student():
    def __init__(self, name, section, score1, score2, score3, score4):
        self.name = name
        self.section = section
        self.spanish = score1
        self.english = score2
        self.science = score3
        self.socials = score4
        

    #def show_details(self):
        #print(f"Student's name: {self.name}, Section: {self.section}, Spanish Score: {self.spanish}, English Score: {self.english}, Science Score: {self.science}, Socials Score: {self.socials}")

    #def get_average(self):
        #self.average = (self.spanish + self.english + self.science + self.socials) / 4
        #print(f"Average score: {self.average}")


def get_student_info():

    name = input("Student name: ")
    section = input("Section: ")
    spanish = int(input("Spanish Score: "))
    english = int(input("English Score: "))
    science = int(input("Science Score: "))
    socials = int(input("Socials Score: "))

    student_details = Student(name, section, spanish, english, science, socials)

    return student_details




def register_student():
    students = []

    while True:
        new_student = get_student_info()
        students.append(new_student)


        more_info = input("Do you want to add more students information? (yes/no): ")
        if more_info.lower() != 'yes':
            break
        
        
    return students


def show_top_3(n):
    ranking=[]
    for lists in n:
        average1= (lists.spanish + lists.english + lists.science + lists.socials)/4
        names = (lists.name)
        ranking.append([names, average1])
        

    sorted_average = sorted(ranking, key=lambda scores: scores[1], reverse=True)
    top_3 = sorted_average[:3]
    

    print(f'These are the top 3 students with their average score: {top_3}')

def show_students(lst):
    information = []
    for lists in lst:
        information.append([lists.name, lists.section, lists.spanish, lists.english, lists.science, lists.socials])
        
    return information


    
def show_global_scores(score):
    scores = []
    for lists in score:
        all_scores_average = (lists.spanish+ lists.english+ lists.science+ lists.socials)/4
        scores.append(all_scores_average)
        global_average = sum(scores)/len(scores)

    print(f"This is the global average: {global_average}")


def write_csv_file(students_data, data):
    with open('students_information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)

        writer.writerow(["Name", "Section", "Spanish Score", "English Score", "Science Score", "Socials Score"])

        writer.writerows(data)


def write_file(info):
    students_data = info
    write_csv_file('students_information.csv', students_data)


def read_file(filename):
    object_students = []
    try: 
        with open('students_information.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(row["Name"], row["Section"], int(row["Spanish Score"]), int(row["English Score"]), int(row["Science Score"]), int(row["Socials Score"]))
                object_students.append(student)
                #print(row)
    except FileNotFoundError:
        print("A CSV file has not been exported yet. Create a CSV file first.")

    return object_students

def read_students_entered_information(det):
    for student in det:
        print(f"Student name: {student.name}, Section: {student.section}, Spanish Score: {student.spanish}, English Score: {student.english}, Science Score: {student.science}, Socials Score: {student.socials}")

existing_students = read_file("students_information.csv")
#students_list = register_student()
#student_info = show_students(students_list)
#print(show_students(students_list))
#show_top_3(students_list)
#show_global_scores(students_list)
#write_file(student_info)

read_students_entered_information(existing_students)