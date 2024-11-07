passed = 0
user_list = []
user_grade = input("Enter grade of student  (type 'done' to finish):")
t = 0
             
while user_grade.lower() != 'done': 
    if int(user_grade) >= 40 and int(user_grade) <=100:
     user_list.append(int(user_grade))
     if int(user_grade) >= 75:
      passed += 1
         
    else:
        t += 1
        break 
    user_grade = input("Enter grade of student  (type 'done' to finish):")
if t ==0:

 av = sum(user_list) / len(user_list)
 pp = (passed / len(user_list)) * 100
 print(f"Average grade {av:.2f}")
 print(f"Number of students passed: {passed}")
 print(f"Passing percentage {pp:.2f}")
else: 
    print("invalid grade")
    
    