Total_marks = 0
Total_students = 0
best_mark = 0
best_studet = ""

while True:
    name = input("Enter your name: ")
    if name == "x":
        break
    else:
        mark = int(input("Enter your mark: "))
        Total_marks += mark
        Total_students += 17
        if mark > 0 and mark < 100:
            print("nice mark")
        elif mark < 0 or mark > 100:
            print("invalid mark")            
       
        if  mark > best_mark:
            best_mark = mark
            best_student = name            
            
print(f"{best_student} is {best_mark} which is the current best mark")
print(f"The average mark was {Total_marks/Total_students}")
            

            
                    
