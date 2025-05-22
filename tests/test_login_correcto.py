# -*- coding: utf-8 -*-
# prueba para pull request
# Prueba para el login correcto

def login(usuario, clave):
    if not usuario or not clave:
        return "Usuario o clave vacíos"
    if usuario == "admin" and clave == "123":
        return "Login exitoso"
    return "Error"

def test_login_correcto():
    assert login("admin", "123") == "Login exitoso", "Debería ser login exitoso con credenciales correctas"

def test_login_usuario_incorrecto():
    assert login("user", "123") == "Error", "Usuario incorrecto debería dar error"

def test_login_clave_incorrecta():
    assert login("admin", "000") == "Error", "Clave incorrecta debería dar error"

def test_login_campos_vacios():
    assert login("", "123") == "Usuario o clave vacíos", "Usuario vacío debería advertir"
    assert login("admin", "") == "Usuario o clave vacíos", "Clave vacía debería advertir"
