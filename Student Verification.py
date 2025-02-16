def check_qualification():
    print("=== Student Accommodation Qualification Check ===")
    
    # Get student details
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    registered = input("Are you registered for the current academic year? (yes/no): ").strip().lower()
    matric_province = input("Enter the province where you did your matric: ").strip().lower()
    
    # Check matric province
    if matric_province == "western cape":
        print(f"Sorry, {name} {surname}, students who did matric in the Western Cape are disqualified.")
        return
    
    # Check registration
    if registered != "yes":
        print(f"Sorry, {name} {surname}, you must be registered for the current academic year to qualify.")
        return
    
    # Input marks per module
    marks = []
    num_modules = int(input("Enter the number of modules: "))
    
    if num_modules < 3:
        print(f"Sorry, {name} {surname}, you must input at least 3 modules to qualify.")
        return

    for i in range(1, num_modules + 1):
        mark = int(input(f"Enter the mark for module {i}: "))
        marks.append(mark)

    # Check if all marks are 50% or above
    if all(mark >= 50 for mark in marks):
        print(f"Congratulations, {name} {surname}, you qualify for accommodation.")
    else:
        print(f"Sorry, {name} {surname}, you did not pass all modules and do not qualify for accommodation.")


# Run the function
check_qualification()
