from pruebasoftware.test_ejercicio3 import validar_email() 

def test_email_formato_correcto_juan_perez():
    correo_prueba = "juan.perez@empresa.com"
    esperado = True
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_formato_correcto_maria_89():
    correo_prueba = "maria_89@univ.edu"
    esperado = True
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_formato_correcto_a_b_c():
    correo_prueba = "a.b-c@web-site.net"
    esperado = True
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_formato_correcto_usuario123():
    correo_prueba = "usuario123@mi-dominio.org"
    esperado = True
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_formato_correcto_john_doe():
    correo_prueba = "john.doe@company.io"
    esperado = True
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_sin_arroba():
    correo_prueba = "sin_arroba.com"
    esperado = False
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_con_espacios():
    correo_prueba = "espacios en@correo.com"
    esperado = False
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_sin_extension():
    correo_prueba = "user@dominio"
    esperado = False
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_extension_corta():
    correo_prueba = "nombre@dominio.c"
    esperado = False
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_email_con_caracteres_invalidos():
    correo_prueba = "mal#email@mail.com"
    esperado = False
    resultado = validar_email(correo_prueba)
    assert esperado == resultado, f"Falló: '{correo_prueba}' → Se esperaba {esperado}, pero se obtuvo {resultado}"


if __name__ == "__main__":
    test_email_formato_correcto_juan_perez()
    test_email_formato_correcto_maria_89()
    test_email_formato_correcto_a_b_c()
    test_email_formato_correcto_usuario123()
    test_email_formato_correcto_john_doe()
    test_email_sin_arroba()
    test_email_con_espacios()
    test_email_sin_extension()
    test_email_extension_corta()
    test_email_con_caracteres_invalidos()
    print("Todas las pruebas pasaron correctamente.")

print("Todas las pruebas pasaron correctamente")
