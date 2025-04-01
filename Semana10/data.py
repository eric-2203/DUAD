import csv
import actions


def write_csv_file(students_data, data):
    with open('students_information.csv', mode='a', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)

        writer.writerow(["Name", "Section", "Spanish Score", "English Score", "Socials Score", "Science Score"])

        writer.writerows(data)


def write_file():
    students_data = actions.details
    write_csv_file('students_information.csv', students_data)


def read_file():
    try: 
        with open('students_information.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)
    except FileNotFoundError:
        print("A CSV file has not been exported yet. Create a CSV file first.")



if __name__ == "__main__":
    print("This is a test")