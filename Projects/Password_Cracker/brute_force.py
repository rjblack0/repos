def brute_force(target_password, password_list_file):
    with open(password_list_file, "r") as file:                 #Open Password file
        passwords = file.readlines()

    passwords = [password.strip() for password in passwords]    #Remote any newlines

    for index, password in enumerate(passwords):                #Iterate through them all
        print(f"Trying password {index + 1}: {password}")
        if password == target_password:
            print(f"Password found: {password}")
            return True
    print("Password not found in the list.")
    return False

if __name__ == "__main__":
    target_password = "supersecret"

    password_list_file = "passwords.txt"

    brute_force(target_password, password_list_file)