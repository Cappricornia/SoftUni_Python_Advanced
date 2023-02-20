class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = [".com", ".bg", ".org", ".net"]


while True:
    email = input()
    is_not_valid_email = True
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    for dom in valid_domains:
        if domain.endswith(dom):
            is_not_valid_email = False
            break

    if is_not_valid_email:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

