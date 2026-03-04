def verificacion_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
email = input("Ingrese su correo electrónico: ")
if verificacion_email(email)==True:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
    