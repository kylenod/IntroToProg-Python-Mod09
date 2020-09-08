# ---------------------------------------------------------- #
# Title: Main
# Description: Main body of Assignment09 Script
# ChangeLog (Who,When,What):
# KODonnell,9.7.2020,Created script
# ---------------------------------------------------------- #


# Import Modules
try:
    from DataClasses import Employee as emp
    import ProcessingClasses as PC
    import IOClasses as IO
except Exception as e:
    print(e)

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #

# Declare list of employee objects
lstEmployee = []
print("Welcome to your Employee Database!\n")

# Read data from file

lst = PC.FileProcessor.read_data_from_file("EmployeeData.txt")


for row in lst:
    obj = emp(row[0], row[1], row[2].strip())
    lstEmployee.append(obj)

while True:  # Print menu and prompt user for menu choice
    IO.EmployeeIO.print_menu_items()
    choice = IO.EmployeeIO.input_menu_options()

    if choice.strip() == "1":  #  print current list
        try:
            IO.EmployeeIO.print_current_list_items(lstEmployee)
        except Exception as e:
            print(e)

    elif choice.strip() == "2":  #  add new employee to list
                try:
                    employee = IO.EmployeeIO.input_employee_data()
                    employee.employee_id = employee.employee_id
                    employee.first_name = employee.first_name
                    employee.last_name = employee.last_name
                    lstEmployee = PC.DatabaseProcessor.add_new_employee_to_database(employee, lstEmployee)
                    print(employee.first_name, "saved to your list!")
                except Exception as e:
                    if type(e) == UnboundLocalError:
                        print("Data could not be saved")
                    else:
                        print(e)


    elif choice.strip() == "3":  #  save list to file
        try:
            PC.FileProcessor.save_data_to_file("EmployeeData.txt", lstEmployee)
            print("Data has been saved to file!")
        except Exception as e:
            print(e)

    elif choice.strip() == "4":  #  exit program
        print("Goodbye!")
        break

    else:  #  reprompt for valid input
        print("Please enter an option from the menu (1-4)")