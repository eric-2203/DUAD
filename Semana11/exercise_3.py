import csv

class Student():
    def __init__(self, name, section, score1, score2, score3, score4):
        self.name = name
        self.section = section
        self.spanish = score1
        self.english = score2
        self.science = score3
        self.socials = score4

def create_student():
    while True:
        name = input("Enter the student name: ")
        section = input("Enter the section: ")
        spanish_score = int(input("Enter Spanish score: "))
        english_score = int(input("Enter English score: "))
        science_score = int(input("Enter Science score: "))
        socials_score = int(input("Enter Socials score: "))
        student_info = [name, section, spanish_score, english_score, science_score, socials_score]
        students_list.append(student_info)
        more_info = input("Do you want to add more students information? (yes/no): ")
        if more_info.lower() != 'yes':
            break
    return name, section, spanish_score, english_score, science_score, socials_score

students_list = []
data_student = create_student()

def show_details():
    print(students_list)

def write_csv_file(students_data, data):
    with open('students_information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)

        writer.writerow(["Name", "Section", "Spanish Score", "English Score", "Socials Score", "Science Score"])

        writer.writerows(data)

def write_file():
    students_data = students_list
    write_csv_file('students_information.csv', students_data)

def read_file():
    try: 
        with open('students_information.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)
    except FileNotFoundError:
        print("A CSV file has not been exported yet. Create a CSV file first.")

students = Student(data_student[0], [1], [2], [3], [4], [5])
show_details()
write_file()
read_file()