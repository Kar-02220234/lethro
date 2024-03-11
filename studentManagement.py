students_list = []
students_dict = {}

name = input("enter student's name: ")
age = input("enter student's age:")
grade = input("enter student's grae:")
students_list.append(name)
students_dict[name] = {"age": age,"grade":grade}
print("students detail added successfully! ")

search_students = input("enter the student's name to search: ")
if search_students in students_dict:
    print(f"student found: {name}, age:{students_dict[name]['age']}, grade: {students_dict[name]['grade']}")
else:
    print("information not found!")
    
    
remove_students = input("enter the student's name to remove or enter to skip: ")
if remove_students in students_dict:
    students_list[name]
    del students_dict[name]
    print("student removed successgully!")
else:
    print("student not found!")



