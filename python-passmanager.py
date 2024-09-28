import hashlib # provides hashing algorithms like SHA-256
import getpass # allows password input without displaying it

password_manager = {} # stores key value pairs of username and password

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ") # getpass library hides the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashlib library hashes the password using sha256 alg
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # determines if the user and hashed password match the key value pair in the password_manager dictionary
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful")
    else:
        print("Invalid username or password")
    
def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
