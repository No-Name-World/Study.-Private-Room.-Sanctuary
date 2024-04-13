##############################################ASSIGNMENT##############################################


# Function to submit assignments
def submit_assignment(assignments_data, student_id):
    course_code = input("Enter course code: ")
    assignment_name = input("Enter assignment name: ")
    assignment_status = "Submitted"
    assignments_data.append(f"{student_id},{course_code},{assignment_name}: {assignment_status}\n")
    print("Assignment submitted successfully.")



# Function to check assignment submission status for a student
def check_submission_status(assignments_data, student_id):
    print("Assignment Submission Status:")
    found = False
    for line in assignments_data:
        if line.startswith(student_id):
            print(line.strip())
            found = True
    if not found:
        print("No assignment submissions found for this student.")



# Function to update assignment submission status by faculty
def update_submission_status(assignments_data, course_code, faculty_passkey):
    print("Assignment Submission Status for", course_code)
    for i, line in enumerate(assignments_data):
        if line.startswith(course_code):
            print(i, line.strip())
    
    passkey = input("Enter faculty passkey to proceed: ")
    if passkey != faculty_passkey:
        print("Invalid passkey. Access denied.")
        return

    index_input = input("Enter the index of the assignment to update status: ")
    index_parts = index_input.split(':')
    if len(index_parts) == 2 and index_parts[0].strip().isdigit():
        index = int(index_parts[0].strip())
        if 0 <= index < len(assignments_data):
            status = input("Enter new status (Submitted/Graded/Pending): ")
            assignments_data[index] = index_input + f": {status}\n"  # Update the status
            print("Status updated successfully.")
        else:
            print("Invalid index.")
    else:
        print("Invalid input format. Please enter the index in the correct format.")



# Function to delete or edit an assignment submission status
def delete_or_edit_assignment(assignments_data):
    print("Assignment Submission Status:")
    for i, line in enumerate(assignments_data):
        print(f"{i + 1}. {line.strip()}")

    choice = input("Enter the index of the entry to delete or edit (0 to cancel): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(assignments_data):
            action = input("Do you want to (D)elete or (E)dit this entry? ")
            if action.upper() == 'D':
                del assignments_data[index]
                print("Entry deleted successfully.")
            elif action.upper() == 'E':
                new_status = input("Enter the new status: ")
                assignments_data[index] = assignments_data[index].split(":")[0] + f": {new_status}\n"
                print("Entry edited successfully.")
            else:
                print("Invalid action.")
        else:
            print("Invalid index.")
    else:
        print("Invalid input.")

def display_data(attendance_data, timetable_data, assignments_data):
    print("Attendance Records:")
    for record in attendance_data:
        print("".join(map(str, record)))  # Join the elements of each record with an empty string

    display_timetables(timetable_data)

    print("Assignment Submission Status:")
    for line in assignments_data:
        print(line.strip())


