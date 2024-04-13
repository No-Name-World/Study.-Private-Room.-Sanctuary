##############################################MAIN####################################################


# Main function to run the program
def main():
    attendance_data, timetable_data, assignments_data = read_initial_data()

    while True:
        print("\nClassroom Management System")
        print("1. Mark Attendance")
        print("2. Manage Timetables")
        print("3. Submit Assignment")
        print("4. Check Assignment Submission Status")
        print("5. Update Assignment Submission Status")
        print("6. Display Data")
        print("7. Calculate Attendance Percentage")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            attendance_data = mark_attendance(attendance_data, timetable_data)
        elif choice == "2":
            manage_timetables(timetable_data)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            submit_assignment(assignments_data, student_id)
        elif choice == "4":
            student_id = input("Enter student ID: ")
            check_submission_status(assignments_data, student_id)
        elif choice == "5":
            course_code = input("Enter course code: ")
            faculty_passkey = input("Enter faculty passkey: ")
            action = input("Do you want to (U)pdate or (D)elete an entry? ")
            if action.upper() == 'U':
                update_submission_status(assignments_data, course_code, faculty_passkey)
            elif action.upper() == 'D':
                delete_or_edit_assignment(assignments_data)
            else:
                print("Invalid action.")
        elif choice == "6":
            display_data(attendance_data, timetable_data, assignments_data)
        elif choice == "7":
            student_id = input("Enter student ID: ")
            display_attendance_percentage(attendance_data, student_id)
        elif choice == "8":
            write_updated_data(attendance_data, timetable_data, assignments_data)
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
