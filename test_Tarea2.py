import Tarea2


def test_exito():
    prueba1 = Tarea2.funcion(2, 1)
    # probar funcion para el caso de exito --> sirve
    assert prueba1 == (1, 3, 2)


def test_error():
    prueba2 = Tarea2.funcion(1, 2)
    # error debido que el primer valor es menor que es segundo
    assert prueba2 == -25


def test_error2():
    # verifica el error de tipos y busca un resultado igual a -15
    prueba3 = Tarea2.funcion("a", 2)
    assert prueba3 == -15
