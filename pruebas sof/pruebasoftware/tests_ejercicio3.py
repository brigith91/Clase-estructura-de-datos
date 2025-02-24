# pruebasoftware/ejercicio3.py

def validar_email(email):
    if '@' not in email or email.count('@') != 1:
        return False

    usuario, dominio_extension = email.split('@')
    if not usuario or not all(c.isalnum() or c in "._`" for c in usuario):
        return False

    if '.' not in dominio_extension:
        return False

    dominio, extension = dominio_extension.rsplit('.', 1)
    if not dominio.replace('-', '').isalnum() or not (2 <= len(extension) <= 4) or not extension.isalpha():
        return False

    return True


print ( "ok")