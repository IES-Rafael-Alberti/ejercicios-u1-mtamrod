email = input("Introduce tu correo electrónico: ")

email = email.replace(email[email.find("@")+1:], "ceu.es")

print(email)