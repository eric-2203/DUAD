

def get_score(str):
    global score
    while True: 
        try:
            score = int(input(f'Enter {str} score: '))
            if score < 0 or score > 100:
                raise ValueError()
            
        except ValueError:
            print("The value entered is not valid. Enter a valid value")
            get_score(str)
        return score

details = []
average = []
all_scores = []

def get_info():
    global students_average_score    
    print("Enter student information")

    while True: 
        try:
            name = input("Complete name: ")
            section = input("Section: ")
            spanish = get_score('Spanish')
            english = get_score('English')
            socials = get_score('Socials')
            science = get_score('Science')
        except ValueError:
            print("Invalid value. Enter a number")

        student_information = [name, section, spanish, english, socials, science]

        students_average_score = (spanish+english+socials+science)/4
        top_students = students_average_score
        
        all_scores.append(spanish)
        all_scores.append(english)
        all_scores.append(socials)
        all_scores.append(science)

        ranking = [name, top_students]
        average.append(ranking)
        details.append(student_information)
        more_info = input("Do you want to add more students information? (yes/no): ")
        if more_info.lower() != 'yes':
            break


def get_all_details():
    all_details = details
    return all_details

def show_details():
    print(details)

def show_top_3():
    sorted_average = sorted(average, key=lambda scores: scores[1], reverse=True)
    top_3 = sorted_average[:3]


    print(f'These are the top 3 students with their average score: {top_3}')


def convert_list():
    my_list = details
    my_second_list = ['name', 'section', 'spanish', 'english', 'socials', 'science']

    my_dict = dict(zip(my_second_list, my_list))
    print(my_dict)



def show_global_average():
    global_average = sum(all_scores)/len(all_scores)
    print(f'The global average score is: {global_average}')




if __name__ == "__main__" :
    print("This is a test")