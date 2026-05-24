import smtplib
import random
from email.mime.text import MIMEText

File_name = "store.txt"
sender_email = "youremailaddress/sender emailaddress"
password = "enter your passkey" 

def send_otp(receiver_email):
    otp = random.randint(100000, 999999)
    msg = MIMEText(f"Your verification OTP is: {otp}")
    msg['Subject'] = "OTP Verification"
    msg['From'] = sender_email  #ur email
    msg['To'] = receiver_email  

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("OTP sent successfully!")
        return otp
    except Exception :
        print("Try again (Error occured)")
        return None 
    
def register():
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        otp = send_otp(email)
        try:
            entered_otp = int(input("Enter the OTP which is sent to your email: "))
            if entered_otp == otp:
                file=open(File_name, "a")
                file.write(f"{email}:{password}\n")
                file.close()

                print("Registration successful!")
            else:
                print("Invalid OTP. Registration failed.")
        except Exception:
            print("Invalid input.")
    
def login():
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        try:
            file = open(File_name, "r")
            for line in file:
                stored_email, stored_password = line.strip().split(":")
                if stored_email == email and stored_password == password:
                    otp = send_otp(email)
                    entered_otp = int(input("Enter the OTP sent to your email: "))
                    if entered_otp == otp:
                        print("Login successful!")
                        break
                    break
                else:
                    print("Invalid email or password.")
            file.close()
        except FileNotFoundError:
            print("User not found")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
