def test_login_correcto():
    usuario = "admin"
    clave = "123"
    assert login(usuario, clave) == "Login exitoso"


