print("                  tickets        ")
print("                  *******        ")
age = int(input("enter your age: "))
is_student = input("are you student? (yes/no): ")
#deter discount eligibility
is_eligible = (age <= 12) or ((13 <= age <= 18)(is_student.lower() == "yes"))
#print discount eligibility message 
if is_eligible:
    print("you are eligible for a discount.")
else:
    print("you are not eligible for a discount.")
    
    
