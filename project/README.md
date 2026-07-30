# EASYPAISA CLI BANKING SYSTEM
#### Video Demo: https://youtu.be/Pft0cbVWHPQ
#### Description:

The **EasyPaisa CLI Banking System** is a command-line application built in Python that simulates a modern digital wallet and online banking service. Inspired by real-world financial technology applications, this project allows users to create secure accounts, manage funds, perform peer-to-peer money transfers, and maintain a detailed history of all transactions with real-time CSV data persistence.

---

### Key Features

1. **User Account Management**
   - **Secure Sign-up**: New users can register with a unique username, valid email, and a strong password.
   - **Strict Validation**: Utilizes regex and the `validators` library to enforce email syntax, password complexity (uppercase, lowercase, numbers, special characters, 8–64 chars), and username limits.
   - **Authentication**: Prevents duplicate usernames or email addresses during registration and authenticates existing users upon login.

2. **Dashboard Operations**
   - **Check Balance**: Displays the user's live balance.
   - **Deposit & Withdraw with Fault Tolerance**: Features a 3-attempt error-recovery loop for user inputs. If an invalid value (e.g., non-numeric string like `"CAD"` or a negative number) is entered, the program notifies the user, tracks remaining chances, and prompts again before safely returning to the main dashboard.
   - **Peer-to-Peer Transfer**: Allows users to instantly transfer funds to other registered account holders. Checks recipient existence and ensures sufficient sender balance before committing changes.
   - **Transaction History**: Displays a clean, grid-formatted table of all historical deposits, withdrawals, transfers, and account creation logs using `tabulate`.

3. **Data Persistence**
   - All user account records (`Users.csv`) and transaction history logs (`history.csv`) are saved persistently to disk, ensuring user data remains available across program executions.

---

### Project File Structure

#### 1. `project.py`
This is the core entry point of the application. It contains:
- **Standalone Validation Functions**: `validate_email()`, `validate_password()`, and `validate_username()`. These three functions operate independently without side effects, making them straightforward to unit-test.
- **The `User` Class**: Encapsulates user attribute management (username, email, password, balance) using Python `@property` getters and setters. Handles reading and updating user details inside `Users.csv`.
- **CSV Data Logging**: Functions `initialize_files()`, `log_transaction()`, and `update_balance_in_csv()` ensure flat-file data integrity.
- **Interactive Terminal Menus**: Functions for rendering the main menu, user dashboard, handling menu selection bounds, and guiding the user through retry loops.

#### 2. `test_project.py`
Contains unit tests written for `pytest` to test the standalone helper functions in `project.py`:
- `test_validate_email()` verifies standard email formats, missing domains, missing `@` symbols, and non-string inputs.
- `test_validate_password()` tests password security requirements (length, uppercase/lowercase, digits, special characters).
- `test_validate_username()` ensures names comply with length constraints and non-empty string checks.

#### 3. `requirements.txt`
Lists the external third-party packages required by the application:
- `validators`: Used for robust email verification.
- `tabulate`: Used to format terminal tabular data for history logs.
- `pytest`: Used to run unit test suites.

---

### Design Choices

- **Flat-File CSV vs. SQL Database**: For the scope of this project, CSV files were chosen over a full relational database. CSVs provided a lightweight, transparent way to demonstrate file I/O, `csv.DictReader`, and `csv.DictWriter` operations without requiring external database server setup.
- **Input Error Recovery Loops**: Rather than immediately terminating the program or throwing unhandled runtime exceptions when users enter invalid input (such as entering `"CAD"` for deposit amounts), a three-chance retry mechanism was implemented inside the dashboard loop. This significantly improves user experience.
- **Object-Oriented Encapsulation**: Placing logic like `withdraw()`, `deposit()`, and `transfer()` inside the `User` class ensures that business logic remains attached directly to the user instance, keeping menu interface logic separated from transactional data operations.

---

### How to Run the Project

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
