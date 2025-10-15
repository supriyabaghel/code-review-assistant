import os
import pickle
import sqlite3
import tempfile
import sys

# Hardcoded secret - a very bad practice!
API_KEY = "SECRET_API_KEY_12345"

def hello_world():
    """
    Prints a classic greeting.
    This function is simple and has no vulnerabilities.
    """
    print("Hello, World!")

def add(a, b):
    """
    This function adds two numbers.
    It's a safe function, performing basic arithmetic.
    """
    # Adding comments to increase line count
    # This is a very important calculation.
    # We must ensure it is correct.
    result = a + b
    return result

def subtract(a, b):
    """
    This function subtracts two numbers.
    Also a safe function.
    """
    # More comments for line count.
    # Subtraction is the opposite of addition.
    # Mind-blowing, I know.
    result = a - b
    return result

def get_user_info_vulnerable(username):
    """
    VULNERABILITY: SQL Injection
    This function retrieves user info from a database using an insecure query.
    A malicious user could provide a username like: ' OR 1=1 --
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # The vulnerability is here! Using f-string to build a query.
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        user = None
    
    conn.close()
    return user

def run_system_command_vulnerable(command):
    """
    VULNERABILITY: Command Injection
    This function executes a system command passed as an argument.
    A malicious user could pass something like: 'ls; rm -rf /'
    """
    print("Executing a system command...")
    # The vulnerability is here! Using os.system with user input.
    os.system(command)
    print("Command execution finished.")

class User:
    """
    A simple user class.
    """
    def _init_(self, name, email):
        self.name = name
        self.email = email

def deserialize_data_vulnerable(data):
    """
    VULNERABILITY: Insecure Deserialization
    This function uses pickle to deserialize data, which can execute arbitrary code.
    A malicious user can craft a pickle payload that runs a command.
    """
    print("Deserializing data...")
    # The vulnerability is here!
    try:
        user_object = pickle.loads(data)
        print(f"Deserialized user: {user_object.name}")
        return user_object
    except Exception as e:
        print(f"Failed to deserialize: {e}")
        return None

def check_user_privileges_vulnerable(user_role):
    """
    VULNERABILITY: Use of assert for security checks.
    Asserts can be disabled globally in Python, bypassing this check.
    """
    # This is not a reliable security check.
    assert user_role == 'admin', 'User must be an admin!'
    print("User has admin privileges.")
    return True

def calculate_expression_vulnerable(expression):
    """
    VULNERABILITY: Use of eval() on user input.
    'eval' can execute any Python expression, including malicious ones.
    """
    print(f"Evaluating: {expression}")
    # The vulnerability is here!
    try:
        result = eval(expression)
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"Evaluation failed: {e}")
        return None

def create_temp_file_vulnerable():
    """
    VULNERABILITY: Insecure temporary file creation.
    tempfile.mktemp() is deprecated because it has a race condition.
    Another process could create the file between this check and its use.
    """
    # This is a dangerous way to create a temp file.
    temp_path = tempfile.mktemp()
    print(f"Using insecure temp file path: {temp_path}")
    # A malicious actor could link this path to a sensitive file.
    with open(temp_path, 'w') as f:
        f.write("This is some temporary data.")
    return temp_path
    
# Let's add more lines to reach 200
def dummy_function_1():
    # This is just for padding
    pass

def dummy_function_2():
    # This is just for padding
    pass

def dummy_function_3():
    # This is just for padding
    pass

def dummy_function_4():
    # This is just for padding
    pass

def dummy_function_5():
    # This is just for padding
    pass

def dummy_function_6():
    # This is just for padding
    pass

def dummy_function_7():
    # This is just for padding
    pass
    
def dummy_function_8():
    # This is just for padding
    pass

def dummy_function_9():
    # This is just for padding
    pass

def dummy_function_10():
    # This is just for padding
    pass

# Main execution block
if _name_ == "_main_":
    # A safe operation
    hello_world()
    print(f"The secret key is: {API_KEY}") # Leaking the key in logs
    print("-" * 20)

    # --- Demonstrating Vulnerabilities ---

    # 1. SQL Injection Demo
    print("--- SQL Injection Demo ---")
    # Malicious input
    malicious_username = "' OR 1=1 --"
    get_user_info_vulnerable(malicious_username)
    print("-" * 20)

    # 2. Command Injection Demo
    print("--- Command Injection Demo ---")
    # In Windows, 'dir' lists files. In Linux, it would be 'ls'.
    malicious_command = "dir" if sys.platform == "win32" else "ls -l"
    run_system_command_vulnerable(malicious_command)
    print("-" * 20)

    # 3. Insecure Deserialization Demo
    print("--- Insecure Deserialization Demo ---")
    # A simple pickled object
    innocent_data = pickle.dumps(User("Alice", "alice@example.com"))
    deserialize_data_vulnerable(innocent_data)
    
    # A malicious pickle payload (hypothetical)
    # This is what an attacker would craft to run os.system('echo pwned')
    class MaliciousPayload:
        def _reduce_(self):
            return (os.system, ('echo PWNED by pickle!',))

    malicious_data = pickle.dumps(MaliciousPayload())
    deserialize_data_vulnerable(malicious_data)
    print("-" * 20)

    # 4. Assert Vulnerability Demo
    print("--- Assert Vulnerability Demo ---")
    try:
        check_user_privileges_vulnerable("user")
    except AssertionError as e:
        print(f"Caught expected error: {e}")
    # Note: If you run python with -O flag (python -O dummy.py), the assert will be ignored.
    print("-" * 20)

    # 5. Eval Vulnerability Demo
    print("--- Eval Vulnerability Demo ---")
    calculate_expression_vulnerable("2 + 2")
    calculate_expression_vulnerable("os.getcwd()") # This will run a command!
    print("-" * 20)
    
    # 6. Insecure Temp File Demo
    print("--- Insecure Temp File Demo ---")
    temp_file = create_temp_file_vulnerable()
    print(f"Temp file created at: {temp_file}")
    # Clean up the insecurely created file
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print("Cleaned up temp file.")
    print("-" * 20)

    print("Dummy script finished.")

# We have now passed 200 lines.
# This file is intentionally insecure for testing purposes.
# Do not use any of this code in a real application.
# It is designed to be a playground for security analysis tools.
# The end.