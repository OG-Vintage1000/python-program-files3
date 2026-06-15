print("What are Jalen's scores for each subject?")
# Decided not to use input function; directly input information
course_grades = {"Math": (91, 93, 82, 87), "Science": (71, 73, 82, 49), "History": (81, 79, 96, 72), "English": (81, 61, 69, 70), "PE": ()}
print(course_grades)

def get_average_grades(grades_tuple):
    # Used ChatGPT to develop the code, could not figure it out on my own
    for course, grades in grades_tuple.items():
        total = 0

        for grade in grades:
            total += grade

        average = total / len(grades)
        print(f"The average grade for {course} is {average:.2f}")

try:
    scores = get_average_grades(course_grades)
except:
    print("Error: Performing operation on empty tuple.")