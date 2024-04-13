##############################################DISPLAY#################################################


# Function to display attendance data grouped by student ID
def display_attendance_data(attendance_data):
    student_attendance = {}

    # Group attendance data by student ID
    for key, value in attendance_data.items():
        parts = key.split('-')
        if len(parts) != 4:
            print(f"Issue with key format: {key}. Skipping this entry.")
            continue
        student_id, course_code, datetime, status = parts
        if student_id not in student_attendance:
            student_attendance[student_id] = []
        student_attendance[student_id].append({
            'course_code': course_code,
            'datetime': datetime,
            'status': status
        })

    # Display attendance data for each student
    for student_id, attendance_records in student_attendance.items():
        print(f"\nStudent ID: {student_id}")
        for record in attendance_records:
            print(f"Course Code: {record['course_code']}, Date & Time: {record['datetime']}, Attendance Status: {record['status']}")



# Update display_attendance_submenu() function
def display_attendance_submenu(attendance_data, timetable_data):
    while True:
        print("\nAttendance Options:")
        print("1. Mark Attendance")
        print("2. Calculate Attendance Percentage")
        print("3. Return to Classroom Management System Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance(attendance_data, timetable_data)  # Pass timetable_data here
        elif choice == "2":
            student_id = input("Enter student ID: ")
            calculate_attendance_percentage(attendance_data, student_id)  # Pass student_id here
        elif choice == "3":
            break
        else:
            print("Invalid choice.")



# Function to display the attendance submenu
def display_attendance_submenu(attendance_data, timetable_data):
    while True:
        print("\nAttendance Options:")
        print("1. Mark Attendance")
        print("2. Calculate Attendance Percentage")
        print("3. Return to Classroom Management System Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            mark_attendance(attendance_data, timetable_data)  # Pass timetable_data here
        elif choice == "2":
            calculate_attendance_percentage(attendance_data)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")



# Function to display sub-menu for Assignments
def display_assignments_submenu(assignments_data):
    while True:
        print("\nAssignments Options:")
        print("1. Submit Assignments")
        print("2. Check Assignments")
        print("3. Update Assignment Status (Faculty Members only)")
        print("4. Return to Classroom Management System Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            submit_assignment(assignments_data)
        elif choice == "2":
            check_assignment_status(assignments_data)
        elif choice == "3":
            update_assignment_status(assignments_data)
        elif choice == "4":
            break  # Exit the loop and return to Classroom Management System Menu
        else:
            print("Invalid choice.")



# Function to display data
def display_data(attendance_data, timetable_data, assignments_data):
    while True:
        print("\nDisplay Options:")
        print("1. Display Attendance Data")
        print("2. Display Timetable Data")
        print("3. Display Assignments Data")
        print("4. Display All Data")
        print("5. Return to Classroom Management System Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAttendance Data:")
            for student_id, status in attendance_data.items():
                print(f"Student ID: {student_id}, Attendance Status: {status}")
        elif choice == "2":
            # Display timetable data
            pass
        elif choice == "3":
            # Display assignments data
            pass
        elif choice == "4":
            # Display all data
            print("\nAttendance Data:")
            for student_id, status in attendance_data.items():
                print(f"Student ID: {student_id}, Attendance Status: {status}")

            print("\nTimetable Data:")
            for course_code, details in timetable_data.items():
                print(f"Course Code: {course_code}, Details: {', '.join(details)}")

            print("\nAssignments Data:")
            for key, value in assignments_data.items():
                print(f"Assignment Key: {key}, Submission Status: {value[0]}")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



# Function to handle display options
def handle_display_option(attendance_data, timetable_data, assignments_data):
    while True:
        print("\nDisplay Options:")
        print("1. Display Attendance Data")
        print("2. Display Timetable Data")
        print("3. Display Assignments Data")
        print("4. Display All Data")
        print("5. Return to Classroom Management System Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nAttendance Data:")
            for student_id, status in attendance_data.items():
                print(f"Student ID: {student_id}, Attendance Status: {status}")
        elif choice == "2":
            print("\nTimetable Data:")
            for course_code, details in timetable_data.items():
                print(f"Course Code: {course_code}, Details: {', '.join(details)}")
        elif choice == "3":
            print("\nAssignments Data:")
            for key, value in assignments_data.items():
                print(f"Assignment Key: {key}, Submission Status: {value[0]}")
        elif choice == "4":
            print("\nAttendance Data:")
            for student_id, status in attendance_data.items():
                print(f"Student ID: {student_id}, Attendance Status: {status}")

            print("\nTimetable Data:")
            for course_code, details in timetable_data.items():
                print(f"Course Code: {course_code}, Details: {', '.join(details)}")

            print("\nAssignments Data:")
            for key, value in assignments_data.items():
                print(f"Assignment Key: {key}, Submission Status: {value[0]}")
        elif choice == "5":
            break  
        else:
            print("Invalid choice.")
