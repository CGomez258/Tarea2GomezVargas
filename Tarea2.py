

def funcion(A, B):
    # se debe ingresar los strings con las comillas sino tira el error
    if type(A) != int or type(B) != int:
        return -15 
    # comprobar si la entrada es un numero
    if (A<B):
        # en caso de ser B mayor que A, se retorna el valor -25
        return -25
    else:
        # para cualquier otro caso-> casos correctos se calcula:
        resta = A-B
        # la resta de A-B y lo guarda en la variable resta
        suma = A+B
        # la suma a y b y lo guarda en suma
        multiplicacion = A*B
        # la multiplicación de A y B se guarda en multiplicación
        return(resta, suma, multiplicacion)
        # se retornan los valores en una tupla
