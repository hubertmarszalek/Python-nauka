def user(email, country="Polska", company="Example Ltd"):
    print(f"{email} is {country} in {company}")

user(email="mail@")

user(email="<EMAIL>", country="USA")