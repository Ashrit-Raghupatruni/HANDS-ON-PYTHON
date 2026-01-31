student_id = input("Enter Student Id: ").strip()
email_id = input("Enter Email ID: ").strip()
password = input("Enter Password: ").strip()
referral = input("Enter Referral Code: ").strip()

valid = True

if len(student_id) != 7 or student_id[0:3] != "CSE" or student_id[3] != "-" or not student_id[4:7].isdigit():
    print("Invalid : Student ID format must be CSE-XXX")
    valid = False

if email_id.count("@") != 1:
    print("Invalid : Email_id must contain exactly one '@'")
    valid = False
elif email_id[0] == "@":
    print("Invalid : Email_id must not start with '@'")
    valid = False
elif email_id[-1] == "@":
    print("Invalid : Email_id must not end with '@'")
    valid = False
elif email_id[-4:] != ".edu":
    print("Invalid : Email_id must end with .edu")
    valid = False

if len(password) < 8:
    print("Invalid : Password must be at least 8 characters")
    valid = False
elif not ("A" <= password[0] <= "Z"):
    print("Invalid : Password must start with uppercase letter")
    valid = False
elif not (
    password[0].isdigit() or password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or
    password[4].isdigit() or password[5].isdigit() or password[6].isdigit() or password[7].isdigit()
):
    print("Invalid : Password must contain at least one digit")
    valid = False

if len(referral) != 6 or referral[0:3] != "REF" or referral[5] != "@":
    print("Invalid : Referral code format must be REF##@")
    valid = False
elif not referral[3:5].isdigit():
    print("Invalid : Referral code must contain digits")
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")