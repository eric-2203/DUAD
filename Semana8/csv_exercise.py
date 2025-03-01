import csv



def get_info():
    details = []
    print("Enter game information")
    while True:
        games_information = {
            'name': input("Name: "),
            'gender': input("Gender: "),
            'developer': input("Developer: "),
            'ESRB_classification': input("ESRB Classification: "),
        }
            
        details.append(games_information)
        more_info = input("Do you want to add more games information? (yes/no): ")
        if more_info.lower() != 'yes':
            break
    return details

game_headers = (
    'name',
    'gender',
    'developer',
    'ESRB_classification',
)

def write_csv_file(file_path, data, headers):
    try:
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            if file.tell() == 0:
                writer.writeheader()
                
            writer.writerows(data)
    except IOError:
        print("I/O error")


def main():

    games_data = get_info()
    write_csv_file('games.csv', games_data, game_headers)
        

    

    print("Thank you for the information")

main()