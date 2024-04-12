##############################################Log In##############################################

# Log In 
#
#
#
#
#
#
#
def read_credentials(file_path):
    credentials = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:  # Skip empty lines
                continue
            parts = line.split(",")
            if len(parts) != 3:
                print("Skipping line with invalid format:", line)
                continue
            username = parts[0].strip()
            name = parts[1].strip()
            password = parts[2].strip()
            credentials[username] = (name, password)
    return credentials

def login():
    faculty_credentials = read_credentials("C:\\Users\\User\\Desktop\\HUDSOn CSC1024  FInal 2\\faculty_credentials.txt")
    student_credentials = read_credentials("C:\\Users\\User\\Desktop\\HUDSOn CSC1024  FInal 2\\student_credentials.txt")
    
    print("Welcome To EduHub University!")
    while True:
        print("\nLog In as:")
        print("[1] Student")
        print("[2] Faculty Member")
        print("[3] Exit Program")
        selection = input("Enter your selection: ")
        
        if selection == '1':
            credentials = student_credentials
            user_type = 'Student'
        elif selection == '2':
            credentials = faculty_credentials
            user_type = 'Faculty Member'
        elif selection == '3':
            print("Exiting program.")
            return
        else:
            print("Invalid selection. Please try again.")
            continue
        
        username = input(f"Username ({user_type} ID): ")
        passcode = input("Passcode: ")
        
        if username in credentials and passcode == credentials[username][1]:
            print("Login successful!")
            print("Welcome,", credentials[username][0])
            break
        else:
            print(f"{user_type} Not Found. Please try again.")

if __name__ == "__main__":
    login()
