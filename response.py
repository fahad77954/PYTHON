import validators

email_you = input("what's your email address? ")

if validators.email(email_you):
    print("valid")

else:
    print("invalid")

