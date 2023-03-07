students = {} # Defined a dictionary to store student info
courses = {} # Defined a dictionary to store courses info
marks = {} # Defined a dictionary to store marks info

# Function to insert the number of students and courses: 
def insert_students():
    return int(input("Enter the number of student: "))
def insert_courses():
    return int(input("\nEnter the number of courses: "))

# Function for the student + course info:
def Student__details():
    n_students = insert_students()
    for i in range(n_students):
        s_name = input("\nEnter student name: ")
        s_id = input("\nEnter student id: ")
        s_DoB = input("\nEnter student DoB: ")
        students[s_id] = {"name": s_name, "id": s_id, "DoB": s_DoB}

def Course_details():
    n_courses = insert_courses()
    for i in range(n_courses):
        c_name = input("\nEnter the name of the course: ")
        c_id = input("\nEnter the id of the course: ")
        courses[c_id] = {"name": c_name, "id": c_id}

# Function to insert mark of the course:
def insert_mark():
    c_id = input("\nEnter the id of the course again: ")
    if c_id not in courses:
        return
    for s_id in students:
        mark = float(input(f"\nEnter the mark of {students[s_id]['name']}:"))
        if s_id not in marks:
            marks[s_id] = {}
            marks[s_id][c_id] = mark
#Function to listing the students, courses:
def list_course(courses):
    for c_id in courses:
       print(f"Courses name: {courses[c_id]['name']}")
def list_student(students):
    for s_id in students:
        print(f"Student name: {students[s_id]['name']}")

# Function to show marks of the given courses:
def display_marks():
    c_id = input("Course id: ")
    if c_id not in courses:
        return
    for s_id in students:
        if s_id in marks and c_id in marks[s_id]:
            print(f"(students_id: {students[s_id]['name']}: {marks[s_id][c_id]})")
        else:
            print(f"{students[s_id]['name']}: This student is not in here!? Try again")
        return

# Main program to run: 
Student__details()
Course_details()
insert_mark()
print("Listing students:")
list_student(students)
display_marks()



