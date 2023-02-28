students = [] # Defined a dictionary to store student info
courses = [] # Defined a dictionary to store courses info
marks = [] # Defined a dictionary to store marks info

#Function for the input of students and courses:
def Count_students():
    return int(input("Enter number of students: "))
def Count_courses():
    return int(input("\nEnter number of courses: "))
def Student_detail():
    s_Name = input("\nEnter student name: ")
    s_ID = input("\nEnter student ID: ")
    s_DoB = input("\nEnter DoB of student: ")
    return (s_Name, s_ID, s_DoB)
def Course_detail():
    c_Name = input("\nEnter course name: ")
    c_ID = input("\nEnter course ID: ")
    return (c_Name, c_ID)

#Function for the input of student's marks:
def type_in_marks(course,students):
    mark = int(input(f"\n(Enter the mark for the course{course['c_Name']}: )"))
    course['mark'] = []
    for student in students:
        mark = int(input(f"(Student {student['s_Name']}: )"))
        course['mark'][student['s_ID']] = mark

#Function to listing the students, courses:
def list_course(courses):
    for course in courses:
        print(f"Course ID {course['c_ID']}: ,\n Name {course['c_Name']}: ")
def list_student(students):
    for student in students:
        print(f"Student_ID {student['s_ID']}:, \nName {student['s_Name']}:, \nDoB {student['s_DoB']}: ")
def show_course_mark(courses):
    for s_ID in students:
        if s_ID in marks and courses in marks[s_ID]:
            print(f"(Students_ID: {students[s_ID]['s_Name']}: {marks[s_ID]['c_ID']}")
        else:
            print(f"{students[s_ID]['s_Name']}: Not found!")

# Main function:
n_students = Count_students()
for i in range(n_students):
    students += [Student_detail()]

n_courses = Count_courses()
for i in range(n_courses):
    courses += [Course_detail()]

for course in courses:
    type_in_marks(course, students)
    print("\nListing student:")
    list_student(students)
    print("Show mark: ")
for course in courses:
    show_course_mark(course)

# there is a error in line 22 that said list must be in integer, not string and i quite don't know how to fix
# i have tried but i still can't get it fix, i'm really sorry




