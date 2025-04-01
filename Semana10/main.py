from menu import get_option
import actions
import data
import csv

print("Welcome to the students control system")

def control_system():
    
    while True: 
        selection = get_option()

        if selection == 1:
            actions.get_info()
        elif selection == 2:
            actions.show_details()
        elif selection == 3:
            actions.show_top_3()
        elif selection ==4:
            actions.show_global_average()
        elif selection == 5:
            data.write_file()
        elif selection == 6:
            data.read_file()
        else:
            selection == 7
            break

    print("Thank you for using the system")

control_system()