# Variables and Data Types
"""name = "Testing"
age = 20
fav_prog = ['python','sql']
print(f'My name is {name}, I am {age} years old and my favorite programming language is {fav_prog[0]} ')"""

# Python Functions for Backend Logic
""" def calculate_salary(hours_worked, hourly_rate):
    amount = hours_worked * hourly_rate
    return f"You earned ${amount} this month."
earning = calculate_salary(100, 20)
print(earning) """

#Python Loops & Conditional Statements
""" def bonus_calculator(hours_worked, hourly_rate, performance_score):
    amount = hours_worked * hourly_rate
    if performance_score < 50:
        return f"Your total earnings including bonus are: ${amount}"
    elif performance_score <= 80:
        bonus = amount * 0.05 # 5% bonus
        amount += bonus
        return f"Your total earnings including bonus are: ${amount}"
    else:
        bonus = amount * 0.10 # 10% bonus
        amount += bonus
        return f"Your total earnings including bonus are: ${amount}"
print(bonus_calculator(100, 20, 80)) """

# Python Lists & Dictionary Handling
"""
def display_users(users):
    for user in users:
        print(f"{user['name']} is {user['age']} years old with email {user['email']}.")

# Define users list
users = [
    {"name": "John", "age": 25, "email": "johnwick@gmail.com"},
    {"name": "tested", "age": 24, "email": "tester@gmail.com"}
]

# Call function
display_users(users)
"""

# Python Functions & User Input
""" def register_user():
    name = input("Enter your name: ")
    
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    programming_language = input("Enter your preferred programming language: ")
    user = {"name": name, "age": age, "programming_language": programming_language}
    return user
registered = register_user()
print(registered) """

# Writing to a File
# Saving user data to a file

""" def register_user():
    name = input("Enter your name: ")
    
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    programming_language = input("Enter your preferred programming language: ")
    user = {"name": name, "age": age, "programming_language": programming_language}
    # Appending to the file
    with open("users_data.txt","a") as file:
        file.write(f"{user['name']}, {user['age']}, {user['programming_language']}\n")
 
    print("User data saved successfully!")
register_user() """


# Saving as CSV file
""" import csv

def register_user():
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    programming_language = input("Enter your preferred programming language: ")
    
    # Save data in CSV format
    with open("users_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, programming_language])

    print("User data saved successfully!")

register_user() """

# Reading Data from a File
""" import csv

def display_saved_users():
    try: 
        with open("users_data.csv", "r") as file:
            reader = csv.reader(file)
            print("------ User Data ---")
            for row in reader:
                print(f"Name: {name.strip[]}, Age: {age.strip[]}, Programming Language: {lang.strip[]}")
    except FileNotFoundError:
                print("No user data found")
        
display_saved_users() """

"""

def add_sub():
    while True:
        try:
            num = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
        
    sum_result = num + num2
    print(f"The sum of {num} and {num2} is: {sum_result}")
    
    difference_result = num - num2
    print(f"The difference between {num} and {num2} is: {difference_result}")
add_sub()

"""

""" def profile():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():  # Check if name contains only letters
            break
        else:
            print("Invalid input! Please enter a valid name.")
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    print(f"Your name is {name} and your age is {age}")
            
profile()  """

"""
def grade():
    while True:
        try:
            scores = input("Enter your score: ")
            score = int(scores)
            if score < 0 or score > 100:
                print("Invalid score! Please enter a number between 0 and 100.")
                continue
            if score >= 90:
                print("A")
            elif score >= 80:
                print("B")
            elif score >= 70:
                print("C")
            elif score >= 60:
                print("D")
            elif score >= 50:
                print("E")
            else:
                print("F")
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
        
grade()
"""
# Port Scanner
# This script checks if ports like 80 (web) or 22 (SSH) are open on a target IP.
'''
import socket
target = input("Enter the target IP address: ")
ports = [80, 22, 443, 21, 25]  # Common ports to check
for port in ports:
    s = socket.socket()
    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} is open on {target}")
    s.close() 
'''
"""
age = 25
if age < 18:
        print("You are a minor.")
elif age == 18:
    print("You are just an adult.")
else:
    print("You are older")  
    """
    