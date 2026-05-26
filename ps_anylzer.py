import re

def check_password(password):

    strength = 0

    # LENGTH CHECK
    if len(password) >= 8:
        strength += 1

    # UPPERCASE CHECK
    if re.search(r"[A-Z]", password):
        strength += 1

    # LOWERCASE CHECK
    if re.search(r"[a-z]", password):
        strength += 1

    # NUMBER CHECK
    if re.search(r"[0-9]", password):
        strength += 1

    # SPECIAL CHARACTER CHECK
    if re.search(r"[!@#$%^&*]", password):
        strength += 1

    # PASSWORD RESULT
    print("\n========== PASSWORD ANALYSIS ==========")

    if strength <= 2:

        print("❌ Weak Password")

    elif strength <= 4:

        print("⚠️ Medium Password")

    else:

        print("✅ Strong Password")

    # SHOW DETAILS
    print("\nPassword Details:")

    print("Length >= 8:",
          len(password) >= 8)

    print("Uppercase Present:",
          bool(re.search(r'[A-Z]', password)))

    print("Lowercase Present:",
          bool(re.search(r'[a-z]', password)))

    print("Number Present:",
          bool(re.search(r'[0-9]', password)))

    print("Special Character Present:",
          bool(re.search(r'[!@#$%^&*]', password)))


# USER INPUT
password = input("Enter Password: ")

# CHECK PASSWORD
check_password(password)