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
    #global all_scores
    global average
    
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
    students = []

    while True:
        student = get_student_info()
        students.append(details)


        more_info = input("Do you want to add more students information? (yes/no): ")
        if more_info.lower() != 'yes':
            break
        
        
    return students


def show_top_3(n):
    #average_scores = []
    ranking=[]
    for lists in n:
        average1= (lists[2]+ lists[3]+ lists[4]+lists[5])/4
        names = (lists[0])
        #average_scores.append(names)
        #average_scores.append(average1)
        ranking.append([names, average1])
        

    sorted_average = sorted(ranking, key=lambda scores: scores[1], reverse=True)
    top_3 = sorted_average[:3]
    

    print(f'These are the top 3 students with their average score: {top_3}')

def show_students(lst):
    print(lst)

    
def show_global_scores(score):
    scores = []
    for lists in score:
        all_scores_average = (lists[2]+ lists[3]+ lists[4]+ lists[5])/4
        scores.append(all_scores_average)
        global_average = sum(scores)/len(scores)

    print(f"This is the global average: {global_average}")


def write_csv_file(students_data, data):
    with open('students_information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)

        writer.writerow(["Name", "Section", "Spanish Score", "English Score", "Socials Score", "Science Score"])

        writer.writerows(data)


def write_file():
    students_data = students_list
    write_csv_file('students_information.csv', students_data)


students_list = register_student()
#print(students_list)
show_students(students_list)
show_top_3(students_list)
show_global_scores(students_list)
write_file()