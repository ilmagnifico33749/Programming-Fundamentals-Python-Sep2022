
class CustomError_NameTooShortError(Exception):
    """""raise it when the name in the email is less than or equal to 4"""
    pass

class CustomError_MustContainAtSymbolError(Exception):
    """"raise it when there is no "@" in the email"""
    pass

class CustomError_InvalidDomainError(Exception):
    """raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)"""
    pass

def email_validation(email_address):
    email_address = str(email_address)
    email_validity = True
    email_name = str(email_address[0:(email_address.index("@"))])
    domain = str(email_address[(email_address.index(".")):(len(email_address))])
    print(domain)
    list_valid_domains = [".com", ".bg", ".org", ".net"]

    if len(email_name) <= 4:
        email_validity = False
        raise CustomError_NameTooShortError("Name must be more than 4 characters")

    elif "@" not in email_address:
        email_validity = False
        raise CustomError_MustContainAtSymbolError("Email must contain @")

    elif domain not in list_valid_domains:
        email_validity = False
        raise CustomError_InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if email_validity is True:
        return "Email is valid"


command = input()
while command != "End":
    current_email_address = command
    try:
        print(email_validation(current_email_address))
    except Exception as error:
        print(error)
    command = input()


# ##############################################################################################
# Input_1:
# abc@abv.bg
# ----------------------------------------------------------------------------------------------
# Output_1:
# Traceback (most recent call last):
# File ".\email_validator.py", line 20, in <module>
#     raise NameTooShort("Name must be more than 4 characters")
# __main__.NameTooShort: Name must be more than 4 characters
# ##############################################################################################
# Input_2:
# peter@gmail.com
# petergmail.com
# ----------------------------------------------------------------------------------------------
# Output_2:
# Email is valid
# Traceback (most recent call last):
# File ".\email_validator.py", line 18, in <module>
#     raise MustContainAtSymbolError("Email must contain @")
# __main__.MustContainAtSymbolError: Email must contain @
# ##############################################################################################
# Input_3:
# peter@gmail.hotmail
# ----------------------------------------------------------------------------------------------
# Output_3:
# Traceback (most recent call last):
#     File ".\email_validator.py", line 22, in <module>
#         raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
# __main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net
# ##############################################################################################
