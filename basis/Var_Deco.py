'''
username, pswd = "michael", "12345"
def auth(func):
    def wrapper(*args, **kwargs):
        ip_username=input('Please Enter username')
        ip_pswd=input("Please Enter Password")
        if username == ip_username and pswd == ip_pswd:
            result=func(*args, **kwargs)
            print("After authentfication")
        else:
            exit("Either Username or Password is incorrect!")
        return result
    return wrapper

@auth ()
def home():
    print("---The home Main func---")
    return "from home"

res=home()
print(res)
'''


username, pswd = "michael", "12345"


# Add another variable  --> Add another layer
def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            ip_username=input('Please Enter username')
            ip_pswd=input("Please Enter Password")
            if auth_type=="local":
                if username == ip_username and pswd == ip_pswd:
                    result=func(*args, **kwargs)
                    print("After authentfication")
                else:
                    exit("Either Username or Password is incorrect!")
                return result
            elif auth_type=="ldap":
                print("It is Not Sth. I know as of now.")
        return wrapper
    return outer_wrapper

@auth(auth_type="local")
def home():
    print("---The home Main func---")
    return "from home"

@auth(auth_type="ldap")  # Add another variable
def bbs():
    print("---The bbs Main func---")

res=home()
print(res)
bbs()