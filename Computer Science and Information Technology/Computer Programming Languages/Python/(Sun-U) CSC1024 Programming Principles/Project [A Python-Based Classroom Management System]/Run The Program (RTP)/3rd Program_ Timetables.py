##############################################TIMETABLES##############################################


# Define a class to represent Timetable entries
class TimetableEntry:
    def __init__(self, course_code, course_name, instructor, room_number, time_slot):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.room_number = room_number
        self.time_slot = time_slot
        self.assignment_status = "Pending"  



# Function to create a new timetable entry (This function is used to create a new timetable entry with user-provided details.)
def create_timetable_entry():
    print("Enter the details for the new timetable entry:")
    course_code = input("Course Code: ")
    course_name = input("Course Name: ")
    instructor = input("Instructor: ")
    room_number = input("Room Number: ")
    time_slot = input("Time Slot (HH:MM - HH:MM): ")
    
    return TimetableEntry(course_code, course_name, instructor, room_number, time_slot)



# Function to add a new timetable entry to the timetable data
def add_timetable_entry(timetable_data, new_entry):
    timetable_data.append(new_entry)
    print("New entry added to the timetable.")



# Function to modify timetable entry
def modify_timetable_entry(timetable_data):
    course_code = input("Enter the course code of the entry to be modified: ")
    for entry in timetable_data:
        if entry.course_code == course_code:
            choice = input("Do you want to delete this entry? (Yes/No): ")
            if choice.lower() == 'yes':
                timetable_data.remove(entry)
                print("Timetable entry deleted successfully.")
            else:
                print("Current Timetable Entry:")
                print(f"Course Code: {entry.course_code}, Course Name: {entry.course_name}, Instructor: {entry.instructor}, Room Number: {entry.room_number}, Time Slot: {entry.time_slot}")
                print("Enter new details:")
                entry.course_name = input("New Course Name: ")
                entry.instructor = input("New Instructor: ")
                entry.room_number = input("New Room Number: ")
                # Prompt user to enter time slot in correct format
                entry.time_slot = input("New Time Slot (HH:MM - HH:MM, AM/PM): ")
                print("Timetable entry updated successfully.")
            return
    print("Course code not found in the timetable.")

# Function to manage timetables
def manage_timetables(timetable_data):
    while True:
        print("\nTimetables Options:")
        print("1. Add New Timetable")
        print("2. Update Timetable")
        print("3. Delete or Modify Timetable")  # Changed from "Delete Timetable" to "Delete or Modify Timetable"
        print("4. View Timetable")  # Added option to view timetable
        print("5. Press Any Other Key to Return To The Menu")  # Changed from "4. Any Other Key to Return To The Menu" to "5. Press Any Other Key to Return To The Menu"
        choice = input("Enter your choice: ")
        if choice == "1":
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            instructor = input("Enter instructor: ")
            room_number = input("Enter room number: ")
            time_slots = input("Enter time slots: ")
            timetable_data[course_code] = [course_name, instructor, room_number, time_slots]
            print("Timetable added successfully.")
        elif choice == "2":
            course_code = input("Enter course code to update: ")
            if course_code in timetable_data:
                course_name = input("Enter new course name (leave blank to keep unchanged): ")
                instructor = input("Enter new instructor (leave blank to keep unchanged): ")
                room_number = input("Enter new room number (leave blank to keep unchanged): ")
                time_slots = input("Enter new time slots (leave blank to keep unchanged): ")
                if course_name:
                    timetable_data[course_code][0] = course_name
                if instructor:
                    timetable_data[course_code][1] = instructor
                if room_number:
                    timetable_data[course_code][2] = room_number
                if time_slots:
                    timetable_data[course_code][3] = time_slots
                print("Timetable updated successfully.")
            else:
                print("Course code not found.")
        elif choice == "3":
            course_code = input("Enter course code to delete: ")
            if course_code in timetable_data:
                del timetable_data[course_code]
                print("Timetable deleted successfully.")
            else:
                print("Course code not found.")
        elif choice == "4":
            print("\nCurrent Timetable:")
            for course_code, details in timetable_data.items():
                print(f"Course Code: {course_code}, Details: {', '.join(details)}")
        else:
            break



# Function to display timetables
def display_timetables(timetable_data):
    print("Timetable:")
    for i, entry in enumerate(timetable_data, 1):
        print(f"{i}. Course Code: {entry.course_code}, Course Name: {entry.course_name}, Instructor: {entry.instructor}, Room Number: {entry.room_number}, Time Slot: {entry.time_slot}")
    print()  # Add an empty print statement to create a new line after displaying all entries
