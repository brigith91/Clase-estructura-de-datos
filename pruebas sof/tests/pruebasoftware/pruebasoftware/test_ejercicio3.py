from pruebasoftware.tests_ejercicio3 import validar_email


def test_validar_email():
    email = "juan.perez@empresa.com"
    expect = True
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "maria_89@univ.edu"
    expect = True
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "a.b-c@web-site.net"
    expect = True
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "usuario123@mi-dominio.org"
    expect = True
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "john.doe@company.io"
    expect = True
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "sin_arroba.com"
    expect = False
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "espacios en@correo.com"
    expect = False
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "user@dominio"
    expect = False
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "nombre@dominio.c"
    expect = False
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    email = "mal#email@mail.com"
    expect = False
    result = validar_email(email)
    assert expect == result, f" Falló: '{email}' → Se esperaba {expect}, pero se obtuvo {result}"

    print(" Todas las pruebas pasaron correctamente")
