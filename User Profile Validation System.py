full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))

valid = True
space_found = False

if full_name[0] == " " or full_name[len(full_name) - 1] == " ":
    print("Invalid : Full Name should not start or end with a space")
    valid = False
else:
    for ch in full_name:
        if ch == " ":
            space_found = True
            break
    if not space_found:
        print("Invalid : Full Name must contain at least two words")
        valid = False

if valid:
    if "@" not in email or "." not in email:
        print("Invalid : Email must contain '@' and '.'")
        valid = False
    elif email[0] == "@":
        print("Invalid : Email must not start with '@'")
        valid = False
    else:
        for ch in email:
            if 'a' <= ch <= 'z':
                pass
            elif '0' <= ch <= '9':
                pass
            elif ch == '@' or ch == '.':
                pass
            else:
                print("Invalid : Email contains invalid characters")
                valid = False
                break

if valid:
    if len(mobile) != 10:
        print("Invalid : Mobile number must be exactly 10 digits")
        valid = False
    elif mobile[0] == "0":
        print("Invalid : Mobile number must not start with 0")
        valid = False
    else:
        for digit in mobile:
            if digit < '0' or digit > '9':
                print("Invalid : Mobile number must contain only digits")
                valid = False
                break

if valid:
    if age < 18 or age > 60:
        print("Invalid : Age must be between 18 and 60")
        valid = False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")