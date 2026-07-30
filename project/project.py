import csv
import os
import re
import validators
from tabulate import tabulate


# ==============================================================================
# 3 STANDALONE HELPER FUNCTIONS (Required for CS50P pytest)
# ==============================================================================


def validate_email(email):
    """Returns True if email format is valid, otherwise False."""
    if not isinstance(email, str):
        return False
    return bool(validators.email(email))


def validate_password(password):
    """Returns True if password meets all security rules, otherwise False."""
    if not isinstance(password, str):
        return False
    if not (8 <= len(password) <= 64):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_]", password):
        return False
    return True


def validate_username(username):
    """Returns True if username is non-empty and max 20 chars, otherwise False."""
    if not isinstance(username, str):
        return False
    clean_name = username.strip()
    if not clean_name or len(clean_name) > 20:
        return False
    return True


# ==============================================================================
# FILE INITIALIZERS & LOGGING
# ==============================================================================


def initialize_files():
    """Creates Users.csv and history.csv with headers if they do not exist."""
    if not os.path.exists("Users.csv"):
        with open("Users.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["User Names", "e-mails", "Password", "Balance"]
            )
            writer.writeheader()

    if not os.path.exists("history.csv"):
        with open("history.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["Username", "Action", "Amount", "Balance"]
            )
            writer.writeheader()


def log_transaction(username, action, amount, balance):
    """Appends a transaction log entry to history.csv."""
    initialize_files()
    with open("history.csv", "a", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Username", "Action", "Amount", "Balance"]
        )
        writer.writerow(
            {
                "Username": username,
                "Action": action,
                "Amount": f"${amount:.2f}",
                "Balance": f"${balance:.2f}",
            }
        )


# ==============================================================================
# USER CLASS
# ==============================================================================


class User:

    def __init__(self, username, email, password, balance=50.0):
        self.username = username
        self.email = email
        self.password = password
        self._balance = float(balance)

    def save_new_user(self):
        """Validates credentials against existing users and appends to Users.csv."""
        initialize_files()
        usernames, emails = [], []
        with open("Users.csv", "r") as file:
            reader = csv.DictReader(file)
            for credential in reader:
                usernames.append(credential["User Names"])
                emails.append(credential["e-mails"])

        if self.username in usernames:
            raise ValueError("Name already taken!")
        if self.email in emails:
            raise ValueError("This email is already registered. Please use another email.")

        with open("Users.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["User Names", "e-mails", "Password", "Balance"],
            )
            writer.writerow(
                {
                    "User Names": self.username,
                    "e-mails": self.email,
                    "Password": self.password,
                    "Balance": self._balance,
                }
            )

    def update_balance_in_csv(self):
        """Rewrites Users.csv with updated balances."""
        initialize_files()
        users = []
        with open("Users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["User Names"] == self.username:
                    row["Balance"] = str(self._balance)
                users.append(row)

        with open("Users.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["User Names", "e-mails", "Password", "Balance"],
            )
            writer.writeheader()
            writer.writerows(users)

    def withdraw(self, n):
        if n <= 0:
            raise ValueError("Amount must be positive!")
        if n > self._balance:
            raise ValueError("Insufficient Balance.")
        self._balance -= n
        self.update_balance_in_csv()
        log_transaction(self.username, "Withdraw", n, self._balance)

    def deposit(self, n):
        if n <= 0:
            raise ValueError("Amount must be positive!")
        self._balance += n
        self.update_balance_in_csv()
        log_transaction(self.username, "Deposit", n, self._balance)

    def transfer(self, recipient_username, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > self._balance:
            raise ValueError("Insufficient Balance for transfer.")
        if recipient_username == self.username:
            raise ValueError("Cannot transfer money to yourself!")

        initialize_files()
        users = []
        recipient_found = False
        new_recipient_bal = 0.0

        with open("Users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["User Names"] == recipient_username:
                    recipient_found = True
                    new_recipient_bal = float(row["Balance"]) + amount
                    row["Balance"] = str(new_recipient_bal)
                users.append(row)

        if not recipient_found:
            raise ValueError(f"Recipient '{recipient_username}' not found!")

        self._balance -= amount

        for row in users:
            if row["User Names"] == self.username:
                row["Balance"] = str(self._balance)

        with open("Users.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["User Names", "e-mails", "Password", "Balance"],
            )
            writer.writeheader()
            writer.writerows(users)

        log_transaction(
            self.username,
            f"Transfer to {recipient_username}",
            amount,
            self._balance,
        )
        log_transaction(
            recipient_username,
            f"Transfer from {self.username}",
            amount,
            new_recipient_bal,
        )

    @property
    def balance(self):
        return self._balance

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if not validate_password(password):
            raise ValueError("Password does not meet security requirements.")
        self._password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not validate_email(email):
            raise ValueError("Invalid e-mail!")
        self._email = email

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not validate_username(username):
            raise ValueError("Invalid username length.")
        self._username = username.lower().strip()


# ==============================================================================
# MENUS & INTERFACE FUNCTIONS
# ==============================================================================


def menu():
    print("\n=========================================")
    print("           WELCOME TO EASYPAISA          ")
    print("=========================================")
    print("1. Register (Sign Up)")
    print("2. Login")
    print("3. Exit")
    print("=========================================")


def dashboard_menu(username):
    print("\n=========================================")
    print(f"         EASYPAISA DASHBOARD ({username.upper()})")
    print("=========================================")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. Logout")
    print("=========================================")


def get_choice(min_val, max_val):
    """Prompts user for a numeric choice and validates the range."""
    try:
        val = int(input(f"Enter choice ({min_val}-{max_val}): "))
        if val < min_val or val > max_val:
            raise ValueError(
                f"Choice must be between {min_val} and {max_val}."
            )
        return val
    except ValueError as error:
        raise ValueError(
            f"Invalid input! Choice must be between {min_val} and {max_val}."
        ) from error


def register_user():
    print("\n--- ACCOUNT REGISTRATION ---")
    while True:
        try:
            username = input("Name: ")
            email = input("E-mail: ")
            password = input("Password: ")
            user = User(username, email, password)
            user.save_new_user()
            log_transaction(user.username, "Account Created", 0.0, user.balance)
            print(
                "\n================= ACCOUNT CREATED SUCCESSFULLY ================="
            )
            print(f"Username: {user.username}")
            print(f"Email:    {user.email}")
            print(f"Balance:  ${user.balance:.2f}")
            print(
                "================================================================"
            )
            return user
        except ValueError as error:
            print(f"Error: {error}\nPlease try again.\n")


def login_user():
    print("\n--- USER LOGIN ---")
    username = input("Enter Username: ").lower().strip()
    password = input("Enter Password: ")

    initialize_files()
    user_records = {}

    with open("Users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_records[row["User Names"]] = row

    if username in user_records:
        record = user_records[username]
        if record["Password"] == password:
            print(f"\nLogin Successful! Welcome, {username}.")
            return User(
                record["User Names"],
                record["e-mails"],
                record["Password"],
                float(record["Balance"]),
            )
        else:
            print("Error: Incorrect password!")
            return None
    else:
        print("Error: Username not found!")
        return None


def view_history(username):
    print(f"\n--- TRANSACTION HISTORY FOR {username.upper()} ---")
    initialize_files()
    user_history = []
    with open("history.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username:
                user_history.append(
                    [row["Action"], row["Amount"], row["Balance"]]
                )

    if not user_history:
        print("No transaction history found.")
    else:
        print(
            tabulate(
                user_history,
                headers=["Action", "Amount", "Balance"],
                tablefmt="grid",
            )
        )


def user_dashboard(user):
    while True:
        dashboard_menu(user.username)
        try:
            choice = get_choice(1, 6)
        except ValueError as e:
            print(e)
            continue

        if choice == 1:
            print(f"\nYour Current Balance: ${user.balance:.2f}")

        elif choice == 2:
            attempts = 3
            while attempts > 0:
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    user.deposit(amount)
                    print(
                        f"Successfully deposited ${amount:.2f}! New balance:"
                        f" ${user.balance:.2f}"
                    )
                    break
                except ValueError as e:
                    attempts -= 1
                    if "could not convert string to float" in str(e).lower():
                        print("Error: Invalid input! Please enter a numerical amount (e.g., 50 or 100.50).")
                    else:
                        print(f"Error: {e}")

                    if attempts > 0:
                        print(f"You have {attempts} chance(s) left. Please try again.\n")
                    else:
                        print("Too many invalid attempts. Returning to dashboard menu.\n")

        elif choice == 3:
            attempts = 3
            while attempts > 0:
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    user.withdraw(amount)
                    print(
                        f"Successfully withdrew ${amount:.2f}! Remaining balance:"
                        f" ${user.balance:.2f}"
                    )
                    break
                except ValueError as e:
                    attempts -= 1
                    if "could not convert string to float" in str(e).lower():
                        print("Error: Invalid input! Please enter a numerical amount (e.g., 50 or 100.50).")
                    else:
                        print(f"Error: {e}")

                    if attempts > 0:
                        print(f"You have {attempts} chance(s) left. Please try again.\n")
                    else:
                        print("Too many invalid attempts. Returning to dashboard menu.\n")

        elif choice == 4:
            recipient = input("Enter recipient username: ").lower().strip()
            try:
                amount = float(input("Enter amount to transfer: $"))
                user.transfer(recipient, amount)
                print(
                    f"Successfully transferred ${amount:.2f} to {recipient}!"
                    f" New balance: ${user.balance:.2f}"
                )
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 5:
            view_history(user.username)

        elif choice == 6:
            print(f"\nLogging out {user.username}... Goodbye!")
            break


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================


def main():
    initialize_files()
    while True:
        menu()
        try:
            ch = get_choice(1, 3)
        except ValueError as e:
            print(e)
            continue

        if ch == 1:
            user = register_user()
            if user:
                user_dashboard(user)

        elif ch == 2:
            user = login_user()
            if user:
                user_dashboard(user)

        elif ch == 3:
            print("\nThank you for using EasyPaisa! Goodbye.")
            break


if __name__ == "__main__":
    main()
