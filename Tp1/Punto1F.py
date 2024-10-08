# Un portal web requiere un formulario de alta de usuario donde se ingrese,
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
# una función contrasena_valida(contrasena) que devuelva True en caso de
# superar las siguientes validaciones sobre la contraseña proporcionada por el usuario:
# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.
# La salida esperada es la siguiente:
# abc.123 es válida: False
# Abc.123 es válida: False
# AbC.123 es válida: True
# AbC.1 23 es válida: False
# ÁbC.123 es válida: False

import re
def contrasena_valida(contrasena):
    if len(contrasena) > 5 and len(contrasena) < 21:
        if re.search(r"\d", contrasena) and re.search(r"[A-Z].*[A-Z]", contrasena):
            if re.search(r"[$&+,:;=?@#|<>.^*()%!-]", contrasena):
                if " " not in contrasena:
                    return True
    return False

while True:
    contrasena = input("Ingrese una contraseña válida: ")
    if contrasena_valida(contrasena):
        print("Contraseña válida.")
        break
    else:
        print("Contraseña invalida. Vuelva a ingresar una contraseña.")