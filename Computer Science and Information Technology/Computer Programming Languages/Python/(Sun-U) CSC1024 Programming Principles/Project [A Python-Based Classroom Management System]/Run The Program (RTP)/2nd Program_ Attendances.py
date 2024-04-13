##############################################ATTENDANCES##############################################


# Function to display attendance records
def display_attendance_records(attendance_data):
    print("Attendance Records:")
    for record in attendance_data:
        student_id, course_code, present = record
        status = "Present" if present else "Absent"
        print(f"{student_id}, {course_code}, {status}")



# Function to mark attendance
def mark_attendance(attendance_data, timetable_data):
    print("Marking attendance:")
    student_id = input("Enter your Student ID: ")  # Updated prompt to enter student ID

    # Convert current time to datetime format
    current_time = datetime.now().strftime("%H:%M")
    current_datetime = datetime.strptime(current_time, "%H:%M")

    # Iterate through each entry in the timetable data
    for entry in timetable_data:
        class_start_time = entry.time_slot.split(" - ")[0].strip()
        class_end_time = entry.time_slot.split(" - ")[1].strip()
        class_start_datetime = datetime.strptime(class_start_time, "%I:%M %p")
        class_end_datetime = datetime.strptime(class_end_time, "%I:%M %p")
        
        print(f"Course: {entry.course_code}, {entry.course_name}")
        print("Current Time:", current_time)
        print("Class Start Time:", class_start_time)
        print("Class End Time:", class_end_time)

        # Check if the current time falls within the class time slot
        if class_start_datetime <= current_datetime <= class_end_datetime:
            # Calculate the time 15 minutes after the start of the class
            fifteen_minutes_after_start = class_start_datetime + timedelta(minutes=15)
            print("Fifteen Minutes After Start:", fifteen_minutes_after_start.strftime("%H:%M"))
            if current_datetime <= fifteen_minutes_after_start:
                # Allow marking attendance
                print(f"Class: {entry.course_code} ({entry.course_name}), Current Time: {current_time}, Class Start Time: {class_start_time}, Class End Time: {class_end_time}")
                attendance_status = input("Are you present? ((Y)es or (N)o): ")
                if attendance_status.lower() == 'y':
                    attendance_data.append((student_id, entry.course_code, True))
                    print("Attendance marked successfully.")
                elif attendance_status.lower() == 'n':
                    attendance_data.append((student_id, entry.course_code, False))
                    print("Attendance marked as absent.")
                else:
                    print("Invalid input. Please enter (Y)es or (N)o.")
                return attendance_data

    # If no ongoing class found or not within the first 15 minutes of any class, display error message
    print("No ongoing class found or attendance cannot be marked at this time.")
    return attendance_data



# Function to calculate attendance percentage for each student
def calculate_attendance_percentage(attendance_data, student_id):
    total_classes = 0
    attended_classes = 0
    for record in attendance_data:
        if record[0] == student_id:
            total_classes += 1
            if record[2]:  # If student attended the class
                attended_classes += 1
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100



# Function to display attendance percentage for a student
def display_attendance_percentage(attendance_data, student_id):
    percentage = calculate_attendance_percentage(attendance_data, student_id)
    print(f"Attendance Percentage for Student ID {student_id}: {percentage}%")
    
