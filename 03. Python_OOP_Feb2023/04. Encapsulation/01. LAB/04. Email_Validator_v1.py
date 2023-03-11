class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = list(mails)
        self.domains = list(domains)

    def __is_name_valid(self, name) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, mail) -> bool:
        if self.__is_name_valid(mail[(0):(mail.index("@"))]) is True \
                and self.__is_mail_valid(mail[(mail.index("@")+1):(mail.index("."))]) is True \
                and self.__is_domain_valid(mail[(mail.index(".")+1):(len(mail))]) is True:
            return True
        else:
            return False


# ######################################################
# Test_Code_1:
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
# ------------------------------------------------------
# Output_1:
# True
# False
# False
# False
# ######################################################