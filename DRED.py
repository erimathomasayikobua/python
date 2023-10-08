print("Welcome to the Business Registration System!")
print("Please select an option:")
print("1. Register for TIN")
print("2. NSSF Registration")
print("3. Certifications from Local Government Council")
print("4. Provide Feedback")
print("5. Exit")
#input of user choice
while True:
     user_choice = input("Enter you choice (1-5): ")
     if user_choice == "1":
          print("Connecting to the Tax management system...")
     elif user_choice == "2":
          print("Connecting to the NSSF registration system")
     elif user_choice == "3":
          print("Connecting you to the Local Government")
     elif user_choice == "4":
          feedback = input("Please enter your Feedback: ")
          print("Please wait for a feedback as we are processing your request")
     elif user_choice == "5":
          print("Thank you for using the Business Registration System, Good Bye!!!")
          break 
     else:
          print("Invalid Request!!! Please Try Again")    