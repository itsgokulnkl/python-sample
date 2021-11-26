# Get username and password from user and validate it 
#1. 

# user DB - step 1
user_db={
	"username" : "stamil",
	"password" : "stamil210502" 
}

# store 10 user data

ten_user_data = [{
	"username" : "stamil",
	"password" : "stamil210502" 
},
{
	"username" : "bharath",
	"password" : "test1234" 
},
{
	"username" : "gokul",
	"password" : "gokul@123" 
},
{
	"username" : "rishi",
	"password" : "rishi@123" 
}]

# get user input
username = input("enter your username : ")
password = input("enter your password : ") 

print("on step 1",username,password)

for user in ten_user_data:
	# If condition on step 2
	if username == user['username'] and password == user['password']:
		print("check satisfied")
		break

