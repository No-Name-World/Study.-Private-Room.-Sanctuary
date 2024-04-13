##############################################TXT####################################################


# Function to read initial data from text files
def read_initial_data():
    # Read attendance data
    with open("attendance_StudentID.txt", "r") as file:
        attendance_data = file.readlines()

    # Read timetables data
    with open("timetables_StudentID.txt", "r") as file:
        timetable_data = []
        for line in file.readlines():
            timetable_entry = line.strip().split(',')
            # Clean up time slot data (replace non-breaking space with regular space)
            timetable_entry[4] = timetable_entry[4].replace("\xa0", " ")
            timetable_data.append(TimetableEntry(*timetable_entry))

    # Read assignments data
    with open("assignments_StudentID.txt", "r") as file:
        assignments_data = file.readlines()

    return attendance_data, timetable_data, assignments_data



# Function to write updated data to text files
def write_updated_data(attendance_data, timetable_data, assignments_data):
    # Write updated attendance data
    with open("attendance_StudentID.txt", "w") as file:
        file.writelines(attendance_data)

    # Write updated timetables data
    with open("timetables_StudentID.txt", "w") as file:
        for entry in timetable_data:
            file.write(f"{entry.course_code},{entry.course_name},{entry.instructor},{entry.room_number},{entry.time_slot}\n")

    # Write updated assignments data
    with open("assignments_StudentID.txt", "w") as file:
        file.writelines(assignments_data)
