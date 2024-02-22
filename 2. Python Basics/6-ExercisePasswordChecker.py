# Exercise Password Checker
#This program asks for your credentials, then determines how long your passwrd is and outputs back to the user with the password hidden

username = input('Enter your username:')
password = input('Enter you password:')

hidden_passwd = len(password) * '*' #determines legnth of password provided by user and 
print(f'Hello {username}, your password {hidden_passwd} is {len(password)} letters long.')