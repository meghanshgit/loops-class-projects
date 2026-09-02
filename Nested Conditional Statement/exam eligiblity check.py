# Exam Eligibility Check

attendence = int(input("Enter the attendence percentage : "))

if attendence >= 75:
    med_cert = input("Do you have medical certicate (y or n) : ")
    if med_cert == 'y':
        print("you are allowed for the exam")
    else:
        print("Please get the medical certificate")
else:

    print("You are not eligible to write the exam")