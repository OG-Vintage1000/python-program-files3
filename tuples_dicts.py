# List all the months in a tuple
print("Let's put all the months of the year into a tuple.")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
# months1 = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
print(months)
# Print first and last month
print(f"The first month is {months[0]} and the last month is {months[-1]}.")

"""jump = months[0]
joy = months[-1]
print(f"The first month is {jump} and the last month is {joy}.")"""

print()
# Test run for individual errors on tuples.
try:
    print("Let's append a new element into our 'months' tuple.")
    months.append("Ophiuchus")
    print(months)
except:
    print(f"Error: Tuples are immutable, cannot add element to tuple.")

print()

try:
    print("Let's insert a new element into our 'months' tuple.")
    months.insert(0, "Ophiuchus")
    print(months)
except:
    print(f"Error: Tuples are immutable, cannot add element to tuple.")

print()

try:
    print("Let's delete an element from our 'months' tuple.")
    del months[2]
    print(months)
except:
    print(f"Error: Tuples are immutable, cannot delete element from tuple.")

print()

# Test run for tuple error block using if/elif statements
try:
    print("We're going to make some changes to the 'months' tuple.")
    option = int(input("How are we going to change our tuple? \n" \
    "1: Append\n2: Insert\n3: Delete\n"))
    if option == 1:
        print("Let's append a new element into our 'months' tuple.")
        months.append("Ophiuchus")
        print(months)
    elif option == 2:
        print("Let's insert a new element into our 'months' tuple.")
        months.insert(0, "Ophiuchus")
        print(months)
    elif option == 3:
        print("Let's delete and element from our 'months' tuple.")
        del months[0]
        print(months)
    else:
        print("This choice is not in the list of options.")  
except:
    print(f"Error: Tuples are immutable, cannot add or delete an element from a tuple.")
# It's basic, but gets the job done. Would appreciate suggestions on how to improve code.

print()

"""try:
    num1 = int(input())
    num2 = int(input())
    print((num1 + num2) / 2)
except:
    print("Incorrect value type.")"""

print()

# Dictionary for students and their grades
print("Alright, I need to put student's grades in the gradebook.")

# Creating list for current students and their grades
my_gradebook = {"Samuel": 85, "Jackson": 82, "Micheal": 97, "Jordan": 73}
print(my_gradebook)

print()

# Adding a new student to the gradebook
print("Oh, let me add one more student to the gradebook.")
student = input("Student's name: ")
grade = int(input("Number grade: "))

my_gradebook.update({student: grade})

print(my_gradebook)

print()

print("Let me make a grade correction.")
student = input("Student's name: ")
grade = int(input("Updated grade: "))
my_gradebook[student] = grade
print(my_gradebook)

print()

# Giving a list of students and their grades
print("Here are the grades for this class.")

for student, grade in my_gradebook.items():
    print(student, ":", grade)

"""for student in my_gradebook.keys():
    print(student, ":", my_gradebook[student])"""

print()