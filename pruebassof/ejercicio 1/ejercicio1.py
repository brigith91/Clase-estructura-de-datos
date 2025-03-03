def validar_usuario(nombre):
    if len(nombre) < 5 or len(nombre) > 15:
        return False
    if " " in nombre:
        return False
    if not nombre.isalnum():  # Verifica que solo haya letras y números
        return False
    return True
