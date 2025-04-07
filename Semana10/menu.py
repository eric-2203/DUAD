def get_option():
    print("""
    Options:
    1. Input student information
    2. Check information entered
    3. Check top 3 students
    4. Check students average scores
    5. Export data to a CSV document
    6. Import data previously exported
    7. Exit
    """)
    while True:
        try: 
            option = int(input("Choose an option from the menu: "))
            if option in [1, 2, 3, 4, 5, 6, 7]:
                return option
            else:
                print("Invalid option. Choose an option from the menu")

        except  ValueError:
                print("The value you used is not valid. Select an option from the menu")




if __name__ == "__main__" :
    print("This is a test")