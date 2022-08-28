"list client name with valid email format"
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

print("Welcome to Ulious Solutions \n Please enter your name to further your success.")
clientname = input()
print("Please enter your email:")
clientemail = input()

if __name__ == '__main__':
    email = clientemail
    check(email)
    if (re.fullmatch(regex, email)):
        print(f"Thank you {clientname} for your wise investment let me do the work from here \n again welcome to Ulios Solutions I look forward to working with you!")
        clients = [clientname, clientemail]
        print (clients)
    else:
        print("Sorry that is an invalid email, Please try again.")
else:
    print("An error occurred please try again.")
