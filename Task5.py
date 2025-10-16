correct_username = "alice"
correct_password = "wonderland"
is_2fa_enabled = True
correct_2fa_code = "123456"

input_username = input("Enter username: ")
input_password = input("Enter password: ")
input_2fa_code = input("Enter 2FA code: ")

if (input_username == correct_username and 
    input_password == correct_password and 
    (not is_2fa_enabled or input_2fa_code == correct_2fa_code)):
    print("Login successful!")
else:
    print("Login failed!")