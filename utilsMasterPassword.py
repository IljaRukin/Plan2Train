from werkzeug.security import generate_password_hash,check_password_hash

def setNewPassword():
	password = input("please input your new Password here: ")
	passwordHash = generate_password_hash(password)
	with open("master_password.txt", "w") as f:
		f.write(passwordHash)
	print("set new Password successfully !")

def checkPassword(password):
	with open("master_password.txt", "r") as f:
	    passwordHash = f.readline().replace('\r', '').replace('\n', '')
	return check_password_hash(passwordHash, password)
