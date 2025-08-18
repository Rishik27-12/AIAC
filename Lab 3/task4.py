# Function to register a new user
def register_user(users_db):
    """
    Registers a new user by asking for username and password.
    Stores the credentials in the users_db dictionary.
    """
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter a new password: ")
    users_db[username] = password
    print("User registered successfully!")

# Function to login an existing user
def login_user(users_db):
    """
    Logs in a user by verifying username and password.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Example usage
if __name__ == "__main__":
    users = {}  # Dictionary to store user credentials
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
