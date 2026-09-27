# College Course Management System

users = {
    "teacher": {
        "password": "1234",
        "role": "teacher"
    },
    "student1": {
        "password": "1111",
        "role": "student"
    },
    "student2": {
        "password": "2222",
        "role": "student"
    }
}

students = {
    "student1": {
        "name": "Arun",
        "age": 20,
        "course": "Python",
        "marks": {}
    },

    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "Cyber Security",
        "marks": {}
    }
}

courses = []

def login():

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:

        print("\nLogin successful!")

        role = users[username]["role"]

        if role == "teacher":
            teacher_menu()

        else:
            student_menu(username)

    else:
        print("\nInvalid username or password!")

def add_course():

    course = input("\nEnter course name: ")

    if course in courses:
        print("Course already exists!")
    else:
        courses.append(course)
        print("Course added successfully!")


def add_marks():

    username = input("\nEnter student username: ")

    if username not in students:
        print("Student not found!")
        return

    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))

    students[username]["marks"][subject] = mark

    print("Mark added successfully!")


def view_students():

    print("\n--- Student Records ---")

    for username, data in students.items():

        print("\nUsername:", username)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Course:", data["course"])

        if data["marks"]:
            print("Marks:")

            for subject, mark in data["marks"].items():
                print(subject, ":", mark)

        else:
            print("No marks available.")

def teacher_menu():

    while True:

        print("\n===== TEACHER MENU =====")
        print("1. Add Course")
        print("2. Add Student Marks")
        print("3. View Students")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()

        elif choice == "2":
            add_marks()

        elif choice == "3":
            view_students()

        elif choice == "4":
            print("Teacher logged out.")
            break

        else:
            print("Invalid choice!")

def student_menu(username):

    while True:

        print("\n===== STUDENT MENU =====")
        print("1. View My Details")
        print("2. View My Marks")
        print("3. Calculate Average")
        print("4. View Available Courses")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":

            data = students[username]

            print("\n--- My Details ---")
            print("Name:", data["name"])
            print("Age:", data["age"])
            print("Course:", data["course"])

        elif choice == "2":

            marks = students[username]["marks"]

            print("\n--- My Marks ---")

            if len(marks) == 0:
                print("No marks available.")

            else:
                for subject, mark in marks.items():
                    print(subject, ":", mark)

        elif choice == "3":

            marks = students[username]["marks"]

            if len(marks) == 0:
                print("No marks available.")

            else:
                total = sum(marks.values())
                average = total / len(marks)

                print("Average Mark:", average)

        elif choice == "4":

            print("\n--- Available Courses ---")

            if len(courses) == 0:
                print("No courses available.")

            else:
                for course in courses:
                    print("-", course)

        elif choice == "5":

            print("Student logged out.")
            break

        else:
            print("Invalid choice!")

while True:
    print(" COLLEGE COURSE MANAGEMENT")
    print("==============================")

    print("1. Login")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        login()

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")