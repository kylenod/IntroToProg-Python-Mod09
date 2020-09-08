# ---------------------------------------------------------- #
# Title: Test Harness
# Description: Script for testing Assignment 09 modules
# ChangeLog (Who,When,What):
# KODonnell,9.7.2020,Created script
# ---------------------------------------------------------- #


#Import Modules
try:
    from DataClasses import Employee as emp
    import ProcessingClasses as PC
    import IOClasses as IO
except Exception as e:
    print(e)

lstEmployee = []
try:
    lst = PC.FileProcessor.read_data_from_file("EmployeeData.txt")
    for row in lst:
        obj = emp(row[0].strip(), row[1].strip(), row[2].strip())
        lstEmployee.append(obj)
except Exception as e:
    print(e)


# Test data module
try:
    objP1 = emp(3,"Cecil","Doggo")
    objP2 = emp("sdfasd", "234", "jones")
except Exception as e:
    print(e)

lstEmployee.append(objP1)

# Test IOClasses
IO.EmployeeIO.print_menu_items()
IO.EmployeeIO.input_menu_options()

try:
    objP3 = IO.EmployeeIO.input_employee_data()
except Exception as e:
    print(e)

try:
    lstEmployee = PC.DatabaseProcessor.add_new_employee_to_database(objP3, lstEmployee)
except Exception as e:
    print(e)

IO.EmployeeIO.print_current_list_items(lstEmployee)

try:
    PC.FileProcessor.save_data_to_file("PersonData.txt", lstEmployee)
except Exception as e:
    print(e)

