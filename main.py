# Kylie Anderson
# M02 Lab - Case Study:...else and while.py
# This application takes students names and GPAs and tests if the student qualifies for the Dean's
# list or the Honor Roll.

while True:
    #Promps user inpput for the student's name, or to quit.
    lastName = input("Enter the student's last name. Type ZZZ to quit.: ")
    if lastName == "ZZZ":
        break
    firstName = input("Enter the student's first name: ")
    studentGrade = float(input("Enter the student's GPA: "))
    #Prints the if the student is on the Dean's List or Honor Roll based on the GPA.
    if studentGrade >= 3.5:
        print(firstName, lastName," has made the Dean's List.")
    elif studentGrade >= 3.25:
        print(firstName, lastName," has made the Honor Roll.")