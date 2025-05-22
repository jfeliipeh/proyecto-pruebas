def test_login_correcto():
    usuario = "admin"
    clave = "123"
    assert login(usuario, clave) == "Login exitoso"

def login(usuario, clave):
    if usuario == "admin" and clave == "123":
        return "Login exitoso"
    return "Error"
