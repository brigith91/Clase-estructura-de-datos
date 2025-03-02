from validacion import validar_usuario


def test_validar_usuario():
    # Casos inválidos
    assert validar_usuario("Ana") == False   # Muy corto (menos de 5)
    # Muy largo (más de 15)
    assert validar_usuario("1234567890123456") == False
    assert validar_usuario("Juan_Perez") == False  # Contiene '_'
    assert validar_usuario("User!") == False  # Contiene '!'
    assert validar_usuario("Hello World") == False  # Contiene espacio

    # Casos válidos
    # Letras y números, longitud correcta
    assert validar_usuario("Laura2024") == True
    # Letras y números, longitud correcta
    assert validar_usuario("Pedro5") == True
    assert validar_usuario("A1B2C3") == True  # Letras y números mezclados
    assert validar_usuario("Maria2023") == True  # Nombre con números
    # Nombre dentro del rango permitido
    assert validar_usuario("User12345") == True


if __name__ == "__main__":
    test_validar_usuario()
    print("Todas las pruebas pasaron correctamente.")
