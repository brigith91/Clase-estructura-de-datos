

def validar_email(email):
    """
    Valida si un email tiene el formato correcto.

    Criterios de validación:
    1. No debe contener espacios en blanco.
    2. Debe contener exactamente un '@'.
    3. La parte del usuario (antes del '@') debe estar compuesta solo por caracteres alfanuméricos, puntos (.), guiones bajos (_) o acentos graves (`).
    4. Debe haber un dominio con al menos un punto ('.').
    5. La parte del dominio (después del '@' y antes del último '.') debe ser alfanumérica o contener guiones ('-').
    6. La extensión del dominio debe contener entre 2 y 4 caracteres alfabéticos.

    Parámetros:
        email (str): Dirección de correo electrónico a validar.

    Retorna:
        bool: True si el email es válido, False si no lo es.
    """
    if ' ' in email:
        return False
    if '@' not in email or email.count('@') != 1:
        return False
    usuario_dominio = email.split('@')
    if len(usuario_dominio) != 2:
        return False
    usuario, dominio_extension = usuario_dominio
    if not usuario or not all(c.isalnum() or c in "._`" for c in usuario):
        return False
    if '.' not in dominio_extension:
        return False
    dominio, extension = dominio_extension.rsplit('.', 1)
    if not dominio.replace('-', '').isalnum():
        return False
    if not (2 <= len(extension) <= 4) or not extension.isalpha():
        return False
    return True

print ( "ok")