activities=4
print(f"You have {activities} activities to complete today")

completed_count=0
activity_num=1
activity_name=""

while activity_num<=activities:
    if activity_num==1 :
        activity_name="make your bed"
    elif activity_num==2 :
        activity_name="feed the pet"
    elif activity_num==3 :
        activity_name="take out the trash"
    elif activity_num==4: 
        activity_name="Wash the dish"

    answer=input(f"have you finished: {activity_name}? (yes/no):")

    if answer =="yes":
        completed_count+=1
        activity_num+=1
        print("Great job chore completed .")
    else:
        print("okay, finish it and check again!")

    print("chores remaining :",activities-completed_count)
    print()